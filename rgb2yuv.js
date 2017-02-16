//RGB to YUV converter, based on the code from here:
//                     https://www.mikekohn.net/file_formats/yuv_rgb_converter.php

/////
/////       rgb2yuv
/////
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


/////
/////       yuv2rgb
/////
 function yuv2rgb(f)
{
  var y, u, v, r, g, b;

  var yuv = document.getElementById('yuv');

  //y=parseInt(document.forms[0].y.value);
  //u=parseInt(document.forms[0].u.value);
  //v=parseInt(document.forms[0].v.value);
  y = parseInt(f.y.value);
  u = parseInt(f.u.value);
  v = parseInt(f.v.value);

  r = y + 1.4075 * (v - 128);
  g = y - 0.3455 * (u - 128) - (0.7169 * (v - 128));
  b = y + 1.7790 * (u - 128);

  r = Math.floor(r);
  g = Math.floor(g);
  b = Math.floor(b);

  r = (r < 0) ? 0 : r;
  r = (r > 255) ? 255 : r;

  g = (g < 0) ? 0 : g;
  g = (g > 255) ? 255 : g;

  b = (b < 0) ? 0 : b;
  b = (b > 255) ? 255 : b;

  f.red.value = r;
  f.green.value = g;
  f.blue.value = b;

  r = r.toString(16);
  g = g.toString(16);
  b = b.toString(16);

  if (r.length < 2) { r = "0" + r; }
  if (g.length < 2) { g = "0" + g; }
  if (b.length < 2) { b = "0" + b; }

  yuv.style.background = "#" + r + g + b;
}