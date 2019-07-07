$(document).ready(function() {
  onGetColorList();
});

onAddColor = function() {
  $.ajax({
    type: "POST",
    url: "https://itc-colors.appspot.com/add_color",
    data: {
      color: $('#extColor').val()
    },
    dataType: "json",
    success: function(msg) { 
      onGetColorList();
    },
    error: function(msg) {
      console.log("error");
    }
  });
};

onGetColorList = function() {
  $.ajax({
    type: "GET",
    url: "http://itc-colors.appspot.com/colors",
    dataType: "json",
    success: function(colorArr) {
      colorArr.forEach(color => {
        $("ul").append(`<li>${color["name"]}</li>`);
      });
    },
    error: function(msg) {
      console.log("error");
    }
  });
};
