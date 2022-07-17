'use strict';

const inputField = document.getElementById("search-form--phrase");

if (inputField.parentElement.className.toString().toLowerCase() === "search-form") {
  inputField.onfocus = function () {
    this.parentElement.style.border = "1px solid #0b7285"
    this.parentElement.style.boxShadow = "0 0.6rem 36px rgba(32, 32, 32, 15%)"
  };
  inputField.onblur = function () {
    this.parentElement.style.border = "1px solid #868e96"
    this.parentElement.style.boxShadow = "none"
  };
}
