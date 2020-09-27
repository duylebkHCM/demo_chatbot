//---------------------------------File upload Handler -----------------------------------------

// Get a reference to the progress bar, wrapper & status label
var progress = document.getElementById("progress");
var progress_wrapper = document.getElementById("progress_wrapper");
var progress_status = document.getElementById("progress_status");

// Get a reference to the 3 buttons
var upload_btn = document.getElementById("upload_btn");
var loading_btn = document.getElementById("loading_btn");
var cancel_btn = document.getElementById("cancel_btn");

// Get a reference to the alert wrapper
var alert_wrapper = document.getElementById("alert_wrapper");

// Get a reference to the file input element & input label 
var input = document.getElementById("file_input");
var file_input_label = document.getElementById("file_input_label");

// Function to show alerts
function show_alert(message, alert) {

  alert_wrapper.innerHTML = `
    <div id="alert" class="alert alert-${alert} alert-dismissible fade show" role="alert">
      <span>${message}</span>
      <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
  `
}

// Function to upload file
function upload(url) {

  // Reject if the file input is empty & throw alert
  if (!input.value) {
    show_alert("No file selected", "warning")
    return;
  }

  // Create a new FormData instance
  var data = new FormData();

  // Create a XMLHTTPRequest instance
  var request = new XMLHttpRequest();

  // Set the response type
  request.responseType = "json";

  // Clear any existing alerts
  alert_wrapper.innerHTML = "";

  // Disable the input during upload
  input.disabled = true;

  // Hide the upload button
  upload_btn.classList.add("d-none");

  // Show the loading button
  loading_btn.classList.remove("d-none");

  // Show the cancel button
  cancel_btn.classList.remove("d-none");

  // Show the progress bar
  progress_wrapper.classList.remove("d-none");

  // Get a reference to the file
  var file = input.files[0];

  // Get a reference to the filename
  var filename = file.name;

  // Get a reference to the filesize & set a cookie
  var filesize = file.size;
  document.cookie = `filesize=${filesize}`;

  // Append the file to the FormData instance
  data.append("file", file);

  // request progress handler
  request.upload.addEventListener("progress", function (e) {

    // Get the loaded amount and total filesize (bytes)
    var loaded = e.loaded;
    var total = e.total

    // Calculate percent uploaded
    var percent_complete = (loaded / total) * 100;

    // Update the progress text and progress bar
    progress.setAttribute("style", `width: ${Math.floor(percent_complete)}%`);
    progress_status.innerText = `${Math.floor(percent_complete)}% uploaded`;

  })

  // request load handler (transfer complete)
  request.addEventListener("load", function (e) {

    if (request.status == 200) {

      show_alert(`${request.response.message}`, "success");
    }
    else {
      show_alert(`Error uploading file`, "danger");
    }
    reset();
  });

  // request error handler
  request.addEventListener("error", function (e) {
    reset();
    show_alert(`Error uploading file`, "warning");
  });

  // request abort handler
  request.addEventListener("abort", function (e) {
    reset();
    show_alert(`Upload cancelled`, "primary");
  });

  // Open and send the request
  request.open("post", url);
  request.send(data);

  cancel_btn.addEventListener("click", function () {
    request.abort();
  })
}

// Function to update the input placeholder
function input_filename() {
  file_input_label.innerText = input.files[0].name;
}

// Function to reset the page
function reset() {
  // Clear the input
  input.value = null;

  // Hide the cancel button
  cancel_btn.classList.add("d-none");

  // Reset the input element
  input.disabled = false;

  // Show the upload button
  upload_btn.classList.remove("d-none");

  // Hide the loading button
  loading_btn.classList.add("d-none");

  // Hide the progress bar
  progress_wrapper.classList.add("d-none");

  // Reset the progress bar state
  progress.setAttribute("style", `width: 0%`);

  // Reset the input placeholder
  file_input_label.innerText = "Select file";
}

//------------------------------------------NLU Parse Handler-------------------------------------------
function clear_text(event) {
  console.log("DEBUG event", event.target.id);
  if (event.target.id === "send_btn") {
    // console.log("Hello")
    text_input.value = "";
  }
  else{
    form.elements.namedItem("sentences").value = "";
  }
  return false;
}

function display_pipeline() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}

function logSubmit(event) {
    console.log('DEBUG yes');
    const result = get_input();
    clear_text(event);
    get_reponse_from_rasa(result);
    event.preventDefault();
}

const container = document.getElementById("container");
const form = document.getElementById("my_form"); 
const log = document.getElementById("myDIV");

form.addEventListener("submit", logSubmit); 

function get_input(){
    const text = form.elements.namedItem("sentences").value;
    console.log("DEBUG  text", text);
    return text;
}

function get_reponse_from_rasa(text){

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            //custom action to process this.responseText
            var response = xhttp.responseText
            var json = JSON.parse(response)
            console.log('DEBUG json', json)
            for (x in json){
              log.innerHTML += "<b>" + x +"</b>" + ":";
              log.innerHTML += JSON.stringify(json[x]) + "<br>";
              log.innerHTML += "<br>"
            }
        }
  };
    xhttp.open("POST", "http://localhost:5005/model/parse");
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(JSON.stringify({text: text}));
};

//---------------------------------------Chat box Handler----------------------------------------

const content = document.getElementById("text_res");
const text_input = document.getElementById("text_input");
const box_chat = document.getElementById("form-container");

$("#send_btn").on("click", function(e) {
  var text  = box_chat.elements.namedItem("message").value;
  console.log("DEBUG text", text);

  if (text == "" || $.trim(text) == "") {
      e.preventDefault();
      return false;
  } else {
      send_message(text, "user123");
      clear_text(e);
      e.preventDefault();
      return false;
  }
})

function setUserResponse(message) {
  var UserResponse = '<img class="userAvatar" src=' + "static/img/userAvatar.jpg" + '><p class="userMsg">' + message + ' </p><div class="clearfix"></div>';
  $(UserResponse).appendTo(".chats").show("slow");

  $(".usrInput").val("");
  scrollToBottomOfResults();
  showBotTyping();
  $(".suggestions").remove();
};

function display_response(res) {  
  if (res.length < 1){
    var fallbackMsg = "I am facing some issues, please try again";
    content.innerHTML += '<img class = "botAvatar" src="static/imgs/botAvatar.png"/>' + '<p class="botMsg">' + fallbackMsg + '</p><div class="clearfix"></div>';
  }
  else{
    for (i = 0; i < res.length; i++) {
      if (res[i].hasOwnProperty("text")) {
        content.innerHTML += '<img class = "botAvatar" src="static/imgs/botAvatar.png"/>' + '<p class="botMsg">' + res[i].text + '</p><div class="clearfix"></div>';
      }
      else if (res[i].hasOwnProperty("image")) {
        
      }
    };
  }
  return false;
}

function send_message(message, user_id) {
  content.innerHTML += '<img class = "userAvatar" src="static/imgs/userAvatar.jpg"/>' + '<p class="userMsg">' + message + '</p><div class="clearfix"></div>';

  $.ajax({
    url: "http://localhost:5005/webhooks/rest/webhook",
    type: "POST",
    dataType: 'json',
    contentType: "application/json",
    data: JSON.stringify({message: message, sender: user_id}),
    crossDomain: true,
    success: function(botResponse, status) {
        console.log("Response from Rasa: ", botResponse, "\nStatus: ", status);
        display_response(botResponse);
    },
    error: function(xhr, textStatus, errorThrown) {
      console.log("Error from bot end: ", textStatus);
    }
  });
  return false;
}

function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}