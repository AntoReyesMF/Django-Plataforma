const input = document.querySelector("#slider");
const label = document.querySelector(".mc_label");

input.addEventListener("#slider", event => {
  const value = Number(input.value) / 100;
  input.style.setProperty("--thumb-rotate", `${value * 720}deg`);
  label.innerHTML = Math.round(value *1000);
});