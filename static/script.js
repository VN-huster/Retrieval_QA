// // script.js

// $(document).ready(function () {
//     $("#chat-form").submit(function (event) {
//         event.preventDefault();
//         sendMessage();
//     });

//     $("#user_query").keydown(function (event) {
//         if (event.keyCode === 13) {  // Check if the pressed key is Enter
//             event.preventDefault();
//             sendMessage();
//         }
//     });

//     function sendMessage() {
//         var userInput = $("#user_query").val();

//         // Display the user's message
//         appendToDialog('<p class="user_msg">' + userInput + '</p>');

//         $.ajax({
//             type: "POST",
//             url: "/QAĐHQG",
//             data: JSON.stringify({ "user_input": userInput }),
//             contentType: "application/json;charset=UTF-8",
//             dataType: "text", // Specify that we expect plain text
//             success: function (response) {
//                 console.log(response);
//                 // Display the server's response
//                 appendToDialog('<p class="bot_msg">' + response + '</p>');
//             },
//             error: function (error) {
//                 console.error("Error:", error);
//             }
//         });

//         // Clear the input after sending the message
//         $("#user_query").val("");
//     }

//     function appendToDialog(message) {
//         var dialogHistory = $(".dialog_history");
//         dialogHistory.append(message);
//     }
// });

// script.js

$(document).ready(function () {
    $("#chat-form").submit(function (event) {
        event.preventDefault();
        sendMessage();
    });

    $("#user_query").keydown(function (event) {
        if (event.keyCode === 13) {  // Check if the pressed key is Enter
            event.preventDefault();
            sendMessage();
        }
    });

    function sendMessage() {
        var userInput = $("#user_query").val();

        // Display the user's message
        appendToDialog('<p class="user_msg">' + userInput + '</p>');

        // Determine the correct AJAX URL based on the current page
        var ajaxUrl;
        if (window.location.pathname === '/GPT') {
            ajaxUrl = "/GPT_handle";
        } else if (window.location.pathname === '/VietCuna') {
            ajaxUrl = "/VietCuna_handle";
        } else {
            console.error("Unknown page. Unable to determine AJAX URL.");
            return;
        }

        $.ajax({
            type: "POST",
            url: ajaxUrl,
            data: JSON.stringify({ "user_input": userInput }),
            contentType: "application/json;charset=UTF-8",
            dataType: "text", // Specify that we expect plain text
            success: function (response) {
                console.log(response);
                // Display the server's response
                appendToDialog('<p class="bot_msg">' + response + '</p>');
            },
            error: function (error) {
                console.error("Error:", error);
            }
        });

        // Clear the input after sending the message
        $("#user_query").val("");
    }

    function appendToDialog(message) {
        var dialogHistory = $(".dialog_history");
        dialogHistory.append(message);
    }

    // Function to navigate to another_page
    window.goToVietCuna = function () {
        window.location.href = '/VietCuna';
    };

    // Function to navigate back to GPT
    window.goToGPT = function () {
        window.location.href = '/GPT';
    };
});
