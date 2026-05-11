const sendButton = document.getElementById("sendButton");
const userMessage = document.getElementById("userMessage");
const resultSection = document.getElementById("resultSection");
const quoteText = document.getElementById("quoteText");
const quoteSource = document.getElementById("quoteSource");
const adviceText = document.getElementById("adviceText");

async function fetchEncouragement() {
  const message = userMessage.value.trim();
  const response = await fetch("/api/encourage", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });

  if (!response.ok) {
    quoteText.innerText = "ÍøÂç³ö´íÁË£¬ÇëÉÔºóÔÙÊÔ¡£";
    quoteSource.innerText = "";
    adviceText.innerText = "";
    resultSection.hidden = false;
    return;
  }

  const data = await response.json();
  quoteText.innerText = `¡°${data.quote}¡±`;
  quoteSource.innerText = data.source ? `¡ª¡ª ${data.source}` : "";
  adviceText.innerText = data.advice;
  resultSection.hidden = false;
}

sendButton.addEventListener("click", () => {
  fetchEncouragement();
});

userMessage.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    fetchEncouragement();
  }
});
