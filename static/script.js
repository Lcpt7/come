const form = document.querySelector("#encourageForm");
const messageInput = document.querySelector("#message");
const charHint = document.querySelector("#charHint");
const quoteText = document.querySelector("#quoteText");
const quoteSource = document.querySelector("#quoteSource");
const quoteMeaning = document.querySelector("#quoteMeaning");
const actionText = document.querySelector("#actionText");

messageInput.addEventListener("input", () => {
  const count = messageInput.value.length;
  charHint.textContent = `${count}/400 字`;
});

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const submitButton = form.querySelector("button");
  submitButton.disabled = true;
  submitButton.textContent = "正在生成";

  try {
    const response = await fetch("/api/encourage", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        mood: form.mood.value,
        message: form.message.value,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || "生成失败，请稍后再试。");
    }

    quoteText.textContent = data.quote;
    quoteSource.textContent = `${data.author} · ${data.source}`;
    quoteMeaning.textContent = data.meaning;
    actionText.textContent = data.action;
  } catch (error) {
    quoteText.textContent = "行有不得，反求诸己。";
    quoteSource.textContent = "孟子 · 离娄上";
    quoteMeaning.textContent = error.message;
    actionText.textContent = "刷新页面或稍后再试一次。";
  } finally {
    submitButton.disabled = false;
    submitButton.textContent = "给我一句心力补给";
  }
});
