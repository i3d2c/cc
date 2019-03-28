$(document).ready(() => {
    $("#defaultOpen").click();
})

function openCity(evt, cityName) {
    $(".tabcontent").css("display", "none");
    $(".tablinks").removeClass("active");
    $("#" + cityName).css("display", "block");
    $(evt.target).addClass("active");
} 
