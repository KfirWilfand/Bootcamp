$("#container input").change(function() {
  var buildStr = "";

  $("#container input").each((key, value) => {
    buildStr += $(value).val() + " ";
  });

  $(".results").text(buildStr);
});
