$(document).ready(function() {
  $("#dd-Theme-menu a").click(function(e) {
    theme[`${$(this).attr('id')}`].setTheme();
    $("#dd-Theme-btn").text($(this).text());
  });
});
