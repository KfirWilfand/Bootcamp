$(document).ready(function() {
  setInterval(getAirConState,1000);
});

getAirConState = function() {
  $.ajax({
    type: "GET",
    url: "https://itc-colors.appspot.com/aircon/state",
    dataType: "json",
    success: function(details) {
      if (details["state"] == "on") {
        $("#state").attr("class", "icon son");
        $("#mode").attr("class", "icon m" + details["mode"]).css("display","inline");
        $("#temp").text(details["temp"]).css("display","inline");
      }else{
        $("#state").attr("class", "icon soff");
        $("#mode").css("display","none");
        $("#temp").css("display","none");
      }
    },
    error: function(msg) {
      console.log("error");
    }
  });
};
