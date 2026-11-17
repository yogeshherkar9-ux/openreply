// node seek1.js page.html ms out.png — one frame at an exact time
const {chromium}=require('playwright');const [,,pg,ms,out]=process.argv;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+require('path').resolve(pg));await p.evaluate(()=>document.fonts.ready);
await p.evaluate(t=>document.getAnimations().forEach(a=>{a.pause();a.currentTime=t}),+ms);await p.screenshot({path:out});await b.close()})();
