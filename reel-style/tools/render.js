// node render.js page.html outDir seconds fps [subframes]
// Seeks every CSS animation and screenshots. With subframes>1 it samples a 180° shutter
// (S evenly spaced times inside the first half of each frame) for real motion blur; blend with ffmpeg tmix.
const {chromium} = require('playwright');
const [,, page, out, secs = 6, fps = 30, sub = 1] = process.argv;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1080, height: 1920}});
  await p.goto('file://' + require('path').resolve(page));
  await p.evaluate(() => document.fonts.ready);
  const n = secs * fps, S = +sub;
  let k = 0;
  for (let i = 0; i < n; i++) for (let s = 0; s < S; s++) {
    const t = (i + (S > 1 ? s * 0.5 / S : 0)) * 1000 / fps;
    await p.evaluate(t => document.getAnimations().forEach(a => { a.pause(); a.currentTime = t; }), t);
    await p.screenshot({path: `${out}/f${String(k++).padStart(5, '0')}.jpg`, type: 'jpeg', quality: 95});
  }
  await b.close();
})();
