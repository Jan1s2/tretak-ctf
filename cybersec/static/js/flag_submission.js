document.addEventListener("DOMContentLoaded", function() {
    const alertBox = document.querySelector('#alertBox');

    document.querySelectorAll('.flagForm').forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();

            const formData = new FormData(form);
            const xhr = new XMLHttpRequest();
            xhr.open('POST', form.action, true);
            xhr.setRequestHeader('X-CSRFToken', formData.get('csrfmiddlewaretoken'));

            xhr.onload = function() {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    if (response.valid) {
                        alertBox.className = 'alert alert-success';
                        alertBox.innerText = 'Correct flag!';
                    } else {
                        alertBox.className = 'alert alert-danger';
                        alertBox.innerText = 'Incorrect flag!';
                    }
                    alertBox.style.display = 'block';
                }
            };

            xhr.send(formData);
        });
    });
});
