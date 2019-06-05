from utils import *

# Harris
a = load_image("../data/Rainier1.png")
b = load_image("../data/Rainier2.png")
corners = detect_and_draw_corners(a, 0.25)
save_image(corners, "corners")
print("detect and draw corners done.")

# Patch Matching
matches = find_and_draw_matches(a, b, 0.25)
save_image(matches, "matches")
print("find and draw matches done.")

# Fitting the projection
pan, match_inliners = panorama_image(a, b, 0.18, 2, 50000, 100)
save_image(pan, "easy_panorama")
save_image(match_inliners, "inliners")
print("stitch images done.")
