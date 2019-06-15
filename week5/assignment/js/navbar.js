$(document).ready(function() {
  $("#dd-Theme-menu a").click(function(e) {
    theme[`${$(this).attr("id")}`].setTheme();
    $("#dd-Theme-btn").text($(this).text());
  });

  $("#dd-CardSheet-menu a").click(function(e) {
    cardSet = cards[`${$(this).attr("id")}`];
    $("#dd-CardSheet-btn").text($(this).text());
    buildBoard(cardSet, gameLevel);
  });

  $("#dd-GameLevel-menu a").click(function(e) {
    gameLevel = $(this).attr("id");
    $("#dd-GameLevel-btn").text($(this).text());
    buildBoard(cardSet, gameLevel);
  });

  $("#dd-Theme-menu a").click(function(e) {
    theme[`${$(this).attr("id")}`].setTheme();
    $("#dd-Theme-btn").text($(this).text());
    buildBoard(cardSet, gameLevel);
  });
});
