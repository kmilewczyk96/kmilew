// This JS file fixes some issues with older browsers.
const checkFlexGap = function () {
  const flexEl = document.createElement("div");
  flexEl.style.display = "flex";
  flexEl.style.flexDirection = "column";
  flexEl.style.rowGap = "1px";

  flexEl.appendChild(document.createElement("div"));
  flexEl.appendChild(document.createElement("div"));

  document.body.appendChild(flexEl);
  const isSupported = flexEl.scrollHeight === 1;
  flexEl.parentNode.removeChild(flexEl);

  if (!isSupported) {
    document.body.classList.add("no-flexbox-gap-support");
  }
};

checkFlexGap();
