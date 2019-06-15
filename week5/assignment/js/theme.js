class Theme {
  constructor(name, navbar, navbarBrand, boardColor, backCard) {
    this.name = name;
    this.navbar = navbar;
    this.navbarBrand = navbarBrand;
    this.boardColor = boardColor;
    this.backCard = backCard;
  }

  setTheme() {
    $("#board").css("background-color", this.boardColor);
    $(".navbar").css("background-color", this.navbar);
    $(".navbar-brand").css("color", this.navbarBrand);
    $("#dd-Theme-button").text(this.name);
    $(".card-item").css("background-image", `url(${this.backCard})`);
    currentTheme = this;
  }
}
const theme = {
  itc: new Theme(
    "ITC",
    "#f1f1f1",
    "black",
    "white",
    "./img/theme/itc-backcard.jpg"
  ),
  blue: new Theme(
    "Blue",
    "#5E737F",
    "white",
    "#F6F7EB",
    "./img/theme/blue-backcard.jpg"
  ),
  dark: new Theme(
    "Dark",
    "#23272A",
    "white",
    "#2C2F33",
    "./img/theme/dark-backcard.jpg"
  )
};

$(document).ready(function() {
  theme["itc"].setTheme();

  $("#dd-Theme-menu a").click(function(e) {
    theme[`${$(this).attr("id")}`].setTheme();
    $("#dd-Theme-btn").text($(this).text());
  });
});
