import cv2
import random
import numpy as np
from scipy import signal as sig
from collections import namedtuple

__all__ = [
    "load_image",
    "save_image",
    "detect_corners",
    "compute_descriptor",
    "find_matches",
    "detect_and_draw_corners",
    "find_and_draw_matches",
    "RANSAC",
    "combine_images",
    "panorama_image",
]

# x is related to height, y is related to height
Point = namedtuple("Point", ['x', 'y'])
Descriptor = namedtuple("Descriptor", ['point', 'data'])
Match = namedtuple("Match", ['p', 'q', 'ai', 'bi', 'dist'])

def load_image(fname):
    img = cv2.imread(fname)
    img = np.float32(img)
    return img

def save_image(img, fname):
    cv2.imwrite(fname+".jpg", img)

def detect_corners(im, thresh):
    """ Return the index of corners.

    Args:
        im: image
        thresh: filter out corners
    Return:
        indices: a list of two tuples, first is x indices, second is y indices
    """
    assert len(im.shape) in (2, 3)
    if len(im.shape) == 3:
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    else:
        gray = im
    # corners = cv2.cornerHarris(gray, 2, 3, 0.06)
    kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    Ix = sig.convolve2d(gray, kernel_x, mode='same')
    Iy = sig.convolve2d(gray, kernel_y, mode='same')
    Ixx = Ix*Ix
    Iyy = Iy*Iy
    Ixy = Ix*Iy
    Sxx = cv2.GaussianBlur(Ixx, (3, 3), 2)
    Syy = cv2.GaussianBlur(Iyy, (3, 3), 2)
    Sxy = cv2.GaussianBlur(Ixy, (3, 3), 2)
    det = (Sxx * Syy) - (Sxy * Sxy)
    trace = Sxx + Syy
    k = 0.06
    corners = det - k*(trace * trace)

    # non-maximum suppression
    # if there is a neighbor larger than center, set center to float('-inf')
    w = 2
    for x in range(corners.shape[0]):
        for y in range(corners.shape[1]):
            center = corners[x][y]
            for i in range(x-w, x+w+1):
                for j in range(y-w, y+w+1):
                    if i < 0 or i >= corners.shape[0] or j <0 or j >= corners.shape[1]:
                        continue
                    if corners[i][j] > center:
                        corners[x][y] = float('-inf')
                        break
            if corners[x][y] == float('-inf'):
                break

    # Threshold for an optimal value, it may vary depending on the image.
    indices = np.where(corners > thresh*corners.max())
    return indices

def detect_and_draw_corners(im, thresh):
    """ detect corners and draw them on the image.

    Args:
        im: image
        thresh: threshold to filter out corners
    Return:
        combined: original image painted with corner points
    """
    indices = detect_corners(im, thresh)
    combined = im.copy()
    for x, y in zip(*indices):
        cv2.circle(combined, (int(np.round(y)),int(np.round(x))), 2, (0, 0, 255), 1)
    return combined

def compute_descriptor(img, corners, w=7):
    """ Compute descriptor for each corner pixel

    Args:
        img: image
        corners: a list of x indices and y indices
        w: window size for computing features
    Return:
        des_lst: a list of Descriptor
    """
    assert len(img.shape) == 2, "img must be gray image"
    des_lst = []
    for x, y in zip(*corners):
        point = Point(x, y)
        data = []
        for i in range(x-w, x+w+1):
            for j in range(y-w, y+w+1):
                if i<0 or i>=img.shape[0] or j<0 or j>=img.shape[1]:
                    data.append(0)
                else:
                    data.append(img[i][j] - img[x][y])
        des_lst.append(Descriptor(point, data))
    return des_lst

def l1_distance(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))


def find_matches(a, b, thresh):
    """ Find matches for pair of images

    Args:
        a, b: pair of images
        thresh: threshold for filter out corners
    Return:
        matches: list of matches
    """
    gray_a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    gray_b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
    corners_a = detect_corners(gray_a, thresh)
    corners_b = detect_corners(gray_b, thresh)
    des_a = compute_descriptor(gray_a, corners_a)
    des_b = compute_descriptor(gray_b, corners_b)

    matches = {}
    # find nearest bi for each bi
    for ai, da in enumerate(des_a):
        best = float('inf')
        best_bi = 0
        for bi, db in enumerate(des_b):
            dist = l1_distance(da.data, db.data)
            if dist < best:
                best = dist
                best_bi = bi
                best_db = db
        match = Match(da.point, best_db.point, ai, best_bi, best)

        # remove redundant bi
        if best_bi not in matches:
            matches[best_bi] = match
        elif best < matches[best_bi].dist:
            matches[best_bi] = match
    return list(matches.values())

def find_and_draw_matches(a, b, thresh):
    matches = find_matches(a, b, thresh)
    out = draw_matches(a, b, matches)
    return out

def draw_matches(a, b, matches):
    # draw matches
    # create an empty image
    rows1 = a.shape[0]
    cols1 = a.shape[1]
    rows2 = b.shape[0]
    cols2 = b.shape[1]
    out = np.zeros((max([rows1, rows2]), cols1+cols2, 3), dtype='uint8')
    # place the first image to the left
    out[:rows1, :cols1] = a
    # place the second image to the right
    out[:rows2, cols2:] = b

    # for each pair of points, draw circles, then connect a line
    for match in matches:
        x1, y1 = match.p
        x2, y2 = match.q

        # draw a small circle for each point
        cv2.circle(out, (int(np.round(y1)),int(np.round(x1))), 2, (0, 0, 255), 1)
        cv2.circle(out, (int(np.round(y2)+cols1),int(np.round(x2))), 2, (0, 0, 255), 1)
        # draw line between pair of points
        cv2.line(out, (int(np.round(y1)),int(np.round(x1))), (int(np.round(y2)+cols1),int(np.round(x2))), (0, 0, 255), 1, shift=0)
    return out

def RANSAC(matches, inliner_thresh, iters, cutoff):
    """ Compute homography with RANSAC 

    Args:
        matches: list of matches
        inliner_thresh: threshold to judge whether the point is inliner
        iters: number of iteration
        cutoff: if satisify this, directly return the Hb
    Return:
        Hb: the H satisify cutoff or with best inliners
        best_inliners: The list of inliners with most number
    """
    best = 0
    Hb = None
    best_inliners = None
    fit_num = 4

    for i in range(iters):
        samples = random.sample(matches, fit_num)
        H = compute_homography(samples)
        if H is None: continue
        inliners = model_inliners(H, matches, inliner_thresh)
        if len(inliners) > best:
            Hb = compute_homography(inliners)
            if Hb is None: continue
            best = len(inliners)
            best_inliners = inliners
            if len(inliners) > cutoff:
                print("Find a H beyond cutoff {} with number of inliners {}".format(cutoff, len(inliners)))
                break
    print("The best H with number of inliners: {}".format(best))
    return Hb, best_inliners


def point_distance(p, q):
    return np.sqrt((p.x - q.x)*(p.x - q.x) + (p.y - q.y)*(p.y - q.y))

def project_point(H, p):
    """ project a point p using matrix H """
    _p = np.ones((3, 1))
    _p[0][0] = p.x
    _p[1][0] = p.y
    projected = np.dot(H, _p)
    return Point(projected[0][0], projected[1][0])

def model_inliners(H, matches, thresh):
    """ Find inliner matches after projection 

    Args:
        H: homography matrix
        matches: list of matches
        thresh: threshold to judge whether the point is inline
    Return:
        inliners: list of matches
    """
    count = 0
    inliners = []
    for match in matches:
        pdist =  point_distance(project_point(H, match.p), match.q)
        if pdist < thresh:
            inliners.append(match)
    return inliners

def compute_homography(matches):
    """ compute homography with given matches """
    n = len(matches)
    M, b = [], []
    for match in matches:
        x, y = match.p.x, match.p.y
        xp, yp = match.q.x, match.q.y
        arr1 = [x, y, 1, 0, 0, 0, -x*xp, -y*xp]
        arr2 = [0, 0, 0, x, y, 1, -x*yp, -y*yp]
        M.append(arr1)
        M.append(arr2)
        b.append([xp])
        b.append([yp])
    M = np.array(M)
    b = np.array(b)

    # solve system
    # a = (M^T M)^{-1} M^T b
    try:
        MtMinv = np.linalg.inv(np.dot(M.T, M))
        Mdag = np.dot(MtMinv, M.T)
        a = np.dot(Mdag, b)
        # a, residuals, rank, s = np.linalg.lstsq(M, b)
    except np.linalg.LinAlgError:
        a = None
    # transform to 3x3 matrix
    if a is None:
        H = None
    else:
        data = a.ravel().tolist()
        data.append(1.)
        H = np.array(data).reshape(3, 3)
    return H

def combine_images(a, b, H):
    """ stitch pair of images.

    Args:
        a, b: pair of images
        H: homography matrix
    Return:
        comb: Combined image stitched together
    """
    Hinv = np.linalg.inv(H)
    c1 = project_point(Hinv, Point(0, 0))
    c2 = project_point(Hinv, Point(b.shape[0]-1, 0))
    c3 = project_point(Hinv, Point(0, b.shape[1]-1))
    c4 = project_point(Hinv, Point(b.shape[0]-1, b.shape[1]-1))

    botright_x = max([c1.x, c2.x, c3.x, c4.x])
    botright_y = max([c1.y, c2.y, c3.y, c4.y])
    topleft_x = min([c1.x, c2.x, c3.x, c4.x])
    topleft_y = min([c1.y, c2.y, c3.y, c4.y])
    topleft, botright = Point(topleft_x, topleft_y), Point(botright_x, botright_y)

    dx = min(0, topleft.x)
    dy = min(0, topleft.y)
    dx, dy = int(dx), int(dy)
    w = max(botright.y, a.shape[1]) - dy
    h = max(botright.x, a.shape[0]) - dx
    w, h = int(w), int(h)

    img = np.zeros((h, w, a.shape[2]))
    # paste image a
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            for k in range(a.shape[2]):
                img[i-dx][j-dy][k] = a[i][j][k]

    # paste image b
    for k in range(a.shape[-1]):
        for j in range(int(topleft.y), int(botright.y)):
            for i in range(int(topleft.x), int(botright.x)):
                p = project_point(H, Point(i, j))
                if (int(p.x) >=0 and np.floor(p.x) < b.shape[0]-1 and int(p.y) >= 0 and np.floor(p.y) < b.shape[1]-1):
                    img[i-dx][j-dy][k] = bilinear_interpolate(b, p.x, p.y, k)
    return img

def bilinear_interpolate(img, x, y, c):
    x00 = img[int(np.floor(x))][int(np.floor(y))][c]
    x01 = img[int(np.floor(x))][int(np.ceil(y))][c]
    x10 = img[int(np.ceil(x))][int(np.floor(y))][c]
    x11 = img[int(np.ceil(x))][int(np.ceil(y))][c]
    w1 = y - np.floor(y)
    w2 = np.ceil(y) - y
    w3 = x - np.floor(x)
    w4 = np.ceil(x) - x
    target = w2*w4*x00 + w2*w3*x10 + w1*w4*x01 + w1*w3*x11
    return target

def panorama_image(a, b, thresh, inliner_thresh, iters, cutoff):
    """ Given pair of images, constructh panorama with them

    Return:
        comb: panorama image
        match_inliners: a match image with inlinered matches
    """
    matches = find_matches(a, b, thresh)
    print("Find {} matches".format(len(matches)))
    H, inliners = RANSAC(matches, inliner_thresh, iters, cutoff)
    match_inliners = draw_matches(a, b, inliners)
    comb = combine_images(a, b, H)
    return comb, match_inliners
