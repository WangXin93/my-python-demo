pkg load image;

img = rgb2gray(imread('dog.jpg'));
img = double(img);
[row, col, chs] = size(img);
noise = ones(size(img)) .* 0.2 .* (max(max(img)) - min(min(img)));

for r = 1:row
  for c = 1:col
    if ( rand > 0.5 )
      noise(r, c) = -noise(r, c);
    endif
  endfor
endfor

img_noise = img + noise;
img_const = img + abs(noise);

disp(ssim(img, img_noise));
disp(ssim(img, img_const));