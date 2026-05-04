// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = '#ef4444';
                } else {
                    field.style.borderColor = '#e5e7eb';
                }
            });

            if (!isValid) {
                e.preventDefault();
                alert('Please fill in all required fields');
            }
        });
    });

    // 20-20-20 Rule Reminder (for screen time pages)
    if (document.querySelector('.screen-time-tip')) {
        setInterval(() => {
            showNotification('👁️ Eye Care Reminder: Look 20 feet away for 20 seconds!');
        }, 20 * 60 * 1000); // Every 20 minutes
    }

    // Assessment form enhancement
    const assessmentForm = document.querySelector('.assessment-form');
    if (assessmentForm) {
        const checkboxes = assessmentForm.querySelectorAll('input[type="checkbox"]');
        
        checkboxes.forEach(checkbox => {
            checkbox.addEventListener('change', function() {
                const card = this.closest('.assessment-card');
                if (this.checked) {
                    card.style.background = '#dbeafe';
                    card.style.borderLeft = '4px solid #2563eb';
                } else {
                    card.style.background = '#ffffff';
                    card.style.borderLeft = 'none';
                }
            });
        });
    }

    // Print functionality for disease details
    const printBtn = document.querySelector('.print-btn');
    if (printBtn) {
        printBtn.addEventListener('click', () => {
            window.print();
        });
    }
});

// Notification function
function showNotification(message) {
    if ('Notification' in window && Notification.permission === 'granted') {
        new Notification('Sight Care Portal', {
            body: message,
            icon: '/static/images/eye-icon.png'
        });
    } else {
        // Fallback to alert
        const notification = document.createElement('div');
        notification.className = 'custom-notification';
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #2563eb;
            color: white;
            padding: 1rem 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            z-index: 10000;
            animation: slideIn 0.3s ease;
        `;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 5000);
    }
}

// Request notification permission
if ('Notification' in window && Notification.permission === 'default') {
    Notification.requestPermission();
}