
  
  $('#txt-search').keyup(function(){
      $('.next').prop('disabled', true);
      var searchField = $(this).val();
      if(searchField === '')  {
        $('#filter-records').html('');
        return;
      }
      var regex = new RegExp(searchField, "i");
      var output = '';
      $.each(data, function(key, val){
        var fullname = val.fname +' '+ val.lname;
        if ((fullname.search(regex) != -1)) {
          output += `<li id="${val.id}" class="li-search" name="${val.cost}/${val.quantity}/${val.fname}/${val.lname}">`+ val.fname +' - '+ val.lname +'</li>';
        }
      });
      $('#filter-records').html(output);
  });
  
  $(document).on("click", ".li-search", function () {
    document.getElementById("search_table").hidden = false
    $("#table_body tr").remove();
    $("#txt-search").val($(this).html());
    // setFormFields($(this).attr("id"));
    var nameall = $(this).attr('name').split("/")
    $("#table_body").append(`
    <tr id="${this.id}">
      <td data-label="Book ID">${this.id}</td>
      <td data-label="Name">${nameall[2]}</td>
      <td data-label="Author">${nameall[3]}</td>
      <td data-label="Cost">${nameall[0]}</td>
      <td data-label="Quantity">${nameall[1]}</td>
    </tr>
    `)
    $("#filter-records").html("");
    $(".next").prop("disabled", false);
  });
  
  $(".radio-group .radio").on("click", function () {
    $(".selected .fa").removeClass("fa-check");
    $(".radio").removeClass("selected");
    $(this).addClass("selected");
    if ($("#suser").hasClass("selected") == true) {
      $(".next").prop("disabled", true);
      $(".next").prop("hidden", true);
      $(".searchfield").show();
    } else {
      setFormFields(false);
      $(".next").prop("disabled", false);
      $(".next").prop("hidden", false);
      $("#filter-records").html("");
      $(".searchfield").hide();
    }
  });
  var step = 1;
  $(document).ready(function () { stepProgress(step); });
  
  $(".next").on("click", function () {
    var nextstep = false;
    if (step == 2) {
      nextstep = checkForm("userinfo");
    } else {
      nextstep = true;
    }
    if (nextstep == true) {
      if (step < $(".step").length) {
        $(".step").show();
        $(".step")
          .not(":eq(" + step++ + ")")
          .hide();
        stepProgress(step);
      }
      hideButtons(step);
    }
  });
  
  // ON CLICK BACK BUTTON
  $(".back").on("click", function () {
    if (step > 1) {
      step = step - 2;
      $(".next").trigger("click");
    }
    hideButtons(step);
  });
  
  // CALCULATE PROGRESS BAR
  stepProgress = function (currstep) {
    var percent = parseFloat(100 / $(".step").length) * currstep;
    percent = percent.toFixed();
    $(".progress-bar")
      .css("width", percent + "%")
      .html(percent + "%");
  };
  
  // DISPLAY AND HIDE "NEXT", "BACK" AND "SUMBIT" BUTTONS
  hideButtons = function (step) {
    var limit = parseInt($(".step").length);
    $(".action").hide();
    if (step < limit) {
      $(".next").show();
    }
    if (step > 1) {
      $(".back").show();
    }
    if (step == limit) {
      $(".next").hide();
      $(".submit").show();
    }
  };
  
  function setFormFields(id) {
    if (id != false) {
      // FILL STEP 2 FORM FIELDS
      d = data.find(x => x.id === id);
      console.log(d)
      $('#fname').val(d.fname);
      $('#lname').val(d.lname);
    } else {
      // EMPTY USER SEARCH INPUT
      $("#txt-search").val('');
      // EMPTY STEP 2 FORM FIELDS
      $('#fname').val('');
      $('#lname').val('');
      $('#team').val('');
      $('#address').val('');
      $('#tel').val('');
    }
  }
  
  function checkForm(val) {
    // CHECK IF ALL "REQUIRED" FIELD ALL FILLED IN
    var valid = true;
    $("#" + val + " input:required").each(function () {
      if ($(this).val() === "") {
        $(this).addClass("is-invalid");
        valid = false;
      } else {
        $(this).removeClass("is-invalid");
      }
    });
    return valid;
  }
  