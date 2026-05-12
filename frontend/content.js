function scanParagraphs() {
  let paragraphs = document.querySelectorAll("p");

  paragraphs.forEach((p) => {
    if (p.dataset.scanned) return; // Daha önce kontrol edilmişse atla
    p.dataset.scanned = "true";

    const text = p.innerText;

    console.log("Tespit edilen metin:", text);

    fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: text }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Tahmin sonucu:", data.prediction);

        if (data.prediction === 1) {
          p.style.position = "relative";
          p.style.filter = "blur(3px)";
          p.style.pointerEvents = "none";
          p.title = "⚠️ Sarkastik içerik tespit edildi";

          if (!p.querySelector(".sarcasm-overlay")) {
            const overlay = document.createElement("div");
            overlay.className = "sarcasm-overlay";
            overlay.textContent = "⚠️ Sarkastik içerik";
            overlay.style.position = "absolute";
            overlay.style.top = "10px";
            overlay.style.left = "50%";
            overlay.style.transform = "translateX(-50%)";
            overlay.style.backgroundColor = "transparent"; // arka plan yok
            overlay.style.color = "white"; // beyaz yazı
            overlay.style.textShadow = "0 0 5px black"; // okunabilirlik için gölge
            overlay.style.padding = "4px 10px";
            overlay.style.borderRadius = "5px";
            overlay.style.fontWeight = "bold";
            overlay.style.zIndex = "1000";
            overlay.style.pointerEvents = "none";
            overlay.style.userSelect = "none";
            overlay.style.whiteSpace = "nowrap";

            p.appendChild(overlay);
          }
        }
      })
      .catch((error) => {
        console.error("Hata:", error);
      });
  });
}


const observer = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    mutation.addedNodes.forEach((node) => {
      if (node.nodeType === 1) {
        if (node.tagName === "P") {
          scanParagraphs();
        } else {
          const ps = node.querySelectorAll("p");
          if (ps.length > 0) {
            scanParagraphs();
          }
        }
      }
    });
  });
});

observer.observe(document.body, { childList: true, subtree: true });
scanParagraphs();

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "scanPage") {
    scanParagraphs();
  }
});








