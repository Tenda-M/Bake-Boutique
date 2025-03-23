document.addEventListener('DOMContentLoaded', function () {
    const writeTestimonialButton = document.querySelector('.button-primary');
    if (writeTestimonialButton) {
        writeTestimonialButton.addEventListener('click', () => {
            alert('Redirecting to Write Testimonial Page...');
        });
    }
});
