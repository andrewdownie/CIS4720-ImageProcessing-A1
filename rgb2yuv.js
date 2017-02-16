//RGB to YUV converter, based on the code from here:
//                     https://www.mikekohn.net/file_formats/yuv_rgb_converter.php
function rgb2yuv(f)
{
  var y, u, v, r, g, b;

  var yuv = document.getElementById('yuv');

  r = parseInt(f.red.value);
  g = parseInt(f.green.value);
  b = parseInt(f.blue.value);

  y = r *  .299000 + g *  .587000 + b *  .114000
  u = r * -.168736 + g * -.331264 + b *  .500000 + 128
  v = r *  .500000 + g * -.418688 + b * -.081312 + 128

  f.y.value = Math.floor(y);
  f.u.value = Math.floor(u);
  f.v.value = Math.floor(v);

  r = r.toString(16);
  g = g.toString(16);
  b = b.toString(16);

  if (r.length < 2) { r = "0" + r; }
  if (g.length < 2) { g = "0" + g; }
  if (b.length < 2) { b = "0" + b; }

  yuv.style.background="#" + r + g + b;
 }