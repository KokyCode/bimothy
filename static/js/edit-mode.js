// Edit Mode JavaScript for SA-DOJ Intelligence System
// Handles CRUD operations for all models

// Helper function to get CSRF token
function getCSRFToken() {
    // Try meta tag first
    const metaToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');
    if (metaToken) return metaToken;
    
    // Try hidden input in forms
    const inputToken = document.querySelector('input[name="csrfmiddlewaretoken"]')?.value;
    if (inputToken) return inputToken;
    
    // Try to get from cookie (Django sets csrftoken cookie)
    const cookieValue = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
    
    if (cookieValue) return cookieValue;
    
    console.error('CSRF token not found');
    return '';
}

// Helper function to make API calls
async function apiCall(url, method, data) {
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify(data)
    };
    
    try {
        const response = await fetch(url, options);
        const result = await response.json();
        
        if (!response.ok) {
            throw new Error(result.error || 'Request failed');
        }
        
        return result;
    } catch (error) {
        console.error('API Error:', error);
        alert('Error: ' + error.message);
        throw error;
    }
}

// ===================================
// GANG CRUD OPERATIONS
// ===================================

function openCreateGangModal() {
    document.getElementById('gangId').value = '';
    document.getElementById('gangForm').reset();
    document.getElementById('gangModalTitle').textContent = 'Create New Gang';
    document.getElementById('gangModal').style.display = 'block';
}

function editGang(gangId) {
    // In a real implementation, you would fetch the gang data
    // For now, we'll just open the modal and let the user edit
    document.getElementById('gangId').value = gangId;
    document.getElementById('gangModalTitle').textContent = 'Edit Gang';
    document.getElementById('gangModal').style.display = 'block';
    
    // TODO: Fetch and populate gang data
}

function closeGangModal() {
    document.getElementById('gangModal').style.display = 'none';
}

document.getElementById('gangForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = {
        name: document.getElementById('gangName').value,
        tag: document.getElementById('gangTag').value,
        color: document.getElementById('gangColor').value,
        threat_level: document.getElementById('gangThreatLevel').value,
        member_count: parseInt(document.getElementById('gangMemberCount').value) || 0,
        territory: document.getElementById('gangTerritory').value,
        description: document.getElementById('gangDescription').value,
        is_active: document.getElementById('gangIsActive').checked
    };
    
    const gangId = document.getElementById('gangId').value;
    
    try {
        if (gangId) {
            await apiCall(`/api/gang/${gangId}/update/`, 'POST', formData);
            alert('Gang updated successfully!');
        } else {
            await apiCall('/api/gang/create/', 'POST', formData);
            alert('Gang created successfully!');
        }
        closeGangModal();
        location.reload();
    } catch (error) {
        // Error already handled in apiCall
    }
});

async function deleteGang(gangId) {
    if (!confirm('Are you sure you want to delete this gang? This action cannot be undone.')) {
        return;
    }
    
    try {
        await apiCall(`/api/gang/${gangId}/delete/`, 'POST', {});
        alert('Gang deleted successfully!');
        location.reload();
    } catch (error) {
        // Error already handled in apiCall
    }
}

// ===================================
// MEMBER CRUD OPERATIONS
// ===================================

function openCreateMemberModal() {
    document.getElementById('memberId').value = '';
    document.getElementById('memberForm').reset();
    document.getElementById('memberModalTitle').textContent = 'Create New Member';
    document.getElementById('memberModal').style.display = 'block';
}

function editMember(memberId) {
    document.getElementById('memberId').value = memberId;
    document.getElementById('memberModalTitle').textContent = 'Edit Member';
    document.getElementById('memberModal').style.display = 'block';
    // TODO: Fetch and populate member data
}

function closeMemberModal() {
    document.getElementById('memberModal').style.display = 'none';
}

document.getElementById('memberForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = {
        name: document.getElementById('memberName').value,
        alias: document.getElementById('memberAlias').value,
        gang_id: parseInt(document.getElementById('memberGang').value),
        rank: document.getElementById('memberRank').value,
        threat_level: document.getElementById('memberThreatLevel').value,
        status: document.getElementById('memberStatus').value,
        criminal_record: document.getElementById('memberCriminalRecord').value,
        notes: document.getElementById('memberNotes').value
    };
    
    const memberId = document.getElementById('memberId').value;
    
    try {
        if (memberId) {
            await apiCall(`/api/member/${memberId}/update/`, 'POST', formData);
            alert('Member updated successfully!');
        } else {
            await apiCall('/api/member/create/', 'POST', formData);
            alert('Member created successfully!');
        }
        closeMemberModal();
        location.reload();
    } catch (error) {
        // Error already handled in apiCall
    }
});

async function deleteMember(memberId) {
    if (!confirm('Are you sure you want to delete this member? This action cannot be undone.')) {
        return;
    }
    
    try {
        await apiCall(`/api/member/${memberId}/delete/`, 'POST', {});
        alert('Member deleted successfully!');
        location.reload();
    } catch (error) {
        // Error already handled in apiCall
    }
}

// ===================================
// INCIDENT CRUD OPERATIONS
// ===================================

function openCreateIncidentModal() {
    document.getElementById('incidentId').value = '';
    document.getElementById('incidentForm').reset();
    document.getElementById('incidentModalTitle').textContent = 'Create New Incident';
    document.getElementById('incidentModal').style.display = 'block';
}

function editIncident(incidentId) {
    document.getElementById('incidentId').value = incidentId;
    document.getElementById('incidentModalTitle').textContent = 'Edit Incident';
    document.getElementById('incidentModal').style.display = 'block';
    // TODO: Fetch and populate incident data
}

function closeIncidentModal() {
    document.getElementById('incidentModal').style.display = 'none';
}

document.getElementById('incidentForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = {
        title: document.getElementById('incidentTitle').value,
        incident_type: document.getElementById('incidentType').value,
        location: document.getElementById('incidentLocation').value,
        description: document.getElementById('incidentDescription').value,
        severity: document.getElementById('incidentSeverity').value,
        status: document.getElementById('incidentStatus').value,
        evidence: document.getElementById('incidentEvidence').value
    };
    
    const incidentId = document.getElementById('incidentId').value;
    
    try {
        if (incidentId) {
            await apiCall(`/api/incident/${incidentId}/update/`, 'POST', formData);
            alert('Incident updated successfully!');
        } else {
            await apiCall('/api/incident/create/', 'POST', formData);
            alert('Incident created successfully!');
        }
        closeIncidentModal();
        location.reload();
    } catch (error) {
        // Error already handled in apiCall
    }
});

async function deleteIncident(incidentId) {
    if (!confirm('Are you sure you want to delete this incident? This action cannot be undone.')) {
        return;
    }
    
    try {
        await apiCall(`/api/incident/${incidentId}/delete/`, 'POST', {});
        alert('Incident deleted successfully!');
        location.reload();
    } catch (error) {
        // Error already handled in apiCall
    }
}

// ===================================
// CASE CRUD OPERATIONS
// ===================================

function openCreateCaseModal() {
    document.getElementById('caseId').value = '';
    document.getElementById('caseForm').reset();
    document.getElementById('caseModalTitle').textContent = 'Create New Case';
    document.getElementById('caseModal').style.display = 'block';
}

function editCase(caseId) {
    document.getElementById('caseId').value = caseId;
    document.getElementById('caseModalTitle').textContent = 'Edit Case';
    document.getElementById('caseModal').style.display = 'block';
    // TODO: Fetch and populate case data
}

function closeCaseModal() {
    // Clean up cropper when closing modal
    if (caseImageCropper) {
        caseImageCropper.destroy();
        caseImageCropper = null;
    }
    croppedImageBlob = null;
    document.getElementById('caseModal').style.display = 'none';
}

// Cropper instance for case image
let caseImageCropper = null;
let croppedImageBlob = null;

// Image preview handler for case form with cropping
document.getElementById('caseImage')?.addEventListener('change', function(e) {
    const file = e.target.files[0];
    const preview = document.getElementById('caseImagePreview');
    const cropperContainer = document.getElementById('caseImageCropper');
    const cropperImg = document.getElementById('caseImageCropperImg');
    const removeBtn = document.getElementById('caseImageRemove');
    
    if (file) {
        // Destroy existing cropper if any
        if (caseImageCropper) {
            caseImageCropper.destroy();
            caseImageCropper = null;
        }
        
        const reader = new FileReader();
        reader.onload = function(e) {
            // Show cropper
            cropperImg.src = e.target.result;
            cropperContainer.style.display = 'block';
            preview.innerHTML = '';
            
            // Initialize cropper
            caseImageCropper = new Cropper(cropperImg, {
                aspectRatio: 16 / 9,
                viewMode: 1,
                dragMode: 'move',
                autoCropArea: 0.8,
                restore: false,
                guides: true,
                center: true,
                highlight: false,
                cropBoxMovable: true,
                cropBoxResizable: true,
                toggleable: false,
                zoomable: true,
                scalable: true,
                rotatable: true,
                minCropBoxWidth: 100,
                minCropBoxHeight: 100,
            });
            
            removeBtn.style.display = 'inline-block';
        };
        reader.readAsDataURL(file);
    } else {
        preview.innerHTML = '';
        cropperContainer.style.display = 'none';
        if (caseImageCropper) {
            caseImageCropper.destroy();
            caseImageCropper = null;
        }
        removeBtn.style.display = 'none';
        croppedImageBlob = null;
    }
});

function applyCrop() {
    if (!caseImageCropper) {
        return;
    }
    
    const canvas = caseImageCropper.getCroppedCanvas({
        width: 1200,
        height: 675,
        imageSmoothingEnabled: true,
        imageSmoothingQuality: 'high',
    });
    
    if (canvas) {
        canvas.toBlob(function(blob) {
            croppedImageBlob = blob;
            
            // Show preview of cropped image
            const preview = document.getElementById('caseImagePreview');
            const cropperContainer = document.getElementById('caseImageCropper');
            const imageActions = document.getElementById('caseImageActions');
            
            canvas.toBlob(function(blob) {
                const url = URL.createObjectURL(blob);
                preview.innerHTML = `
                    <img src="${url}" alt="Cropped Preview" style="max-width: 100%; max-height: 200px; border-radius: 8px; margin-top: 10px;">
                    <p style="color: var(--accent-green); font-size: 0.85rem; margin-top: 5px;">✓ Image cropped. Click "Crop Again" to adjust.</p>
                `;
                cropperContainer.style.display = 'none';
                imageActions.style.display = 'block';
            }, 'image/jpeg', 0.9);
        }, 'image/jpeg', 0.9);
    }
}

function cropAgain() {
    const cropperContainer = document.getElementById('caseImageCropper');
    const imageActions = document.getElementById('caseImageActions');
    const cropperImg = document.getElementById('caseImageCropperImg');
    
    if (croppedImageBlob) {
        const url = URL.createObjectURL(croppedImageBlob);
        cropperImg.src = url;
        cropperContainer.style.display = 'block';
        imageActions.style.display = 'none';
        
        // Reinitialize cropper with cropped image
        if (caseImageCropper) {
            caseImageCropper.destroy();
        }
        
        caseImageCropper = new Cropper(cropperImg, {
            aspectRatio: 16 / 9,
            viewMode: 1,
            dragMode: 'move',
            autoCropArea: 0.8,
            restore: false,
            guides: true,
            center: true,
            highlight: false,
            cropBoxMovable: true,
            cropBoxResizable: true,
            toggleable: false,
            zoomable: true,
            scalable: true,
            rotatable: true,
            minCropBoxWidth: 100,
            minCropBoxHeight: 100,
        });
    }
}

function rotateImage(degrees) {
    if (caseImageCropper) {
        caseImageCropper.rotate(degrees);
    }
}

function zoomImage(ratio) {
    if (caseImageCropper) {
        caseImageCropper.zoom(ratio);
    }
}

function resetCrop() {
    if (caseImageCropper) {
        caseImageCropper.reset();
    }
}

function cancelCrop() {
    const cropperContainer = document.getElementById('caseImageCropper');
    const preview = document.getElementById('caseImagePreview');
    const imageActions = document.getElementById('caseImageActions');
    
    if (caseImageCropper) {
        caseImageCropper.destroy();
        caseImageCropper = null;
    }
    
    cropperContainer.style.display = 'none';
    imageActions.style.display = 'none';
    
    // If we had a cropped image, keep the preview. Otherwise clear it.
    if (!croppedImageBlob) {
        preview.innerHTML = '';
    }
}

function removeCaseImage() {
    document.getElementById('caseImage').value = '';
    document.getElementById('caseImagePreview').innerHTML = '';
    document.getElementById('caseImageCropper').style.display = 'none';
    document.getElementById('caseImageActions').style.display = 'none';
    document.getElementById('caseImageRemove').style.display = 'none';
    
    if (caseImageCropper) {
        caseImageCropper.destroy();
        caseImageCropper = null;
    }
    croppedImageBlob = null;
}

document.getElementById('caseForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const caseId = document.getElementById('caseId').value;
    const imageFileInput = document.getElementById('caseImage');
    let imageFile = null;
    
    // Use cropped image if available, otherwise use original file
    if (croppedImageBlob) {
        // Convert blob to file
        const fileName = imageFileInput?.files[0]?.name || 'cropped-image.jpg';
        imageFile = new File([croppedImageBlob], fileName, { type: 'image/jpeg' });
    } else if (imageFileInput?.files[0]) {
        imageFile = imageFileInput.files[0];
    }
    
    // Use FormData if there's an image, otherwise use JSON
    if (imageFile) {
        const formData = new FormData();
        formData.append('case_number', document.getElementById('caseNumber').value);
        formData.append('title', document.getElementById('caseTitle').value);
        formData.append('description', document.getElementById('caseDescription').value);
        formData.append('priority', document.getElementById('casePriority').value);
        formData.append('status', document.getElementById('caseStatus').value);
        formData.append('notes', document.getElementById('caseNotes').value);
        formData.append('image', imageFile);
        
        try {
            const url = caseId ? `/api/case/${caseId}/update/` : '/api/case/create/';
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCSRFToken()
                },
                body: formData
            });
            
            const result = await response.json();
            
            if (!response.ok) {
                throw new Error(result.error || 'Request failed');
            }
            
            alert(caseId ? 'Case updated successfully!' : 'Case created successfully!');
            // Clean up
            if (caseImageCropper) {
                caseImageCropper.destroy();
                caseImageCropper = null;
            }
            croppedImageBlob = null;
            closeCaseModal();
            location.reload();
        } catch (error) {
            console.error('API Error:', error);
            alert('Error: ' + error.message);
        }
    } else {
        // No image, use JSON
        const formData = {
            case_number: document.getElementById('caseNumber').value,
            title: document.getElementById('caseTitle').value,
            description: document.getElementById('caseDescription').value,
            priority: document.getElementById('casePriority').value,
            status: document.getElementById('caseStatus').value,
            notes: document.getElementById('caseNotes').value
        };
        
        // If editing and image should be removed, send empty string
        if (caseId && document.getElementById('caseImageRemove').style.display === 'none' && !imageFile) {
            // Check if there was a previous image that should be kept
            // For now, we'll just not send image field if no new image
        }
        
        try {
            if (caseId) {
                await apiCall(`/api/case/${caseId}/update/`, 'POST', formData);
            alert('Case updated successfully!');
        } else {
            await apiCall('/api/case/create/', 'POST', formData);
            alert('Case created successfully!');
        }
        // Clean up
        if (caseImageCropper) {
            caseImageCropper.destroy();
            caseImageCropper = null;
        }
        croppedImageBlob = null;
        closeCaseModal();
        location.reload();
        } catch (error) {
            // Error already handled in apiCall
        }
    }
});

async function deleteCase(caseId) {
    if (!confirm('Are you sure you want to delete this case? This action cannot be undone.')) {
        return;
    }
    
    try {
        await apiCall(`/api/case/${caseId}/delete/`, 'POST', {});
        alert('Case deleted successfully!');
        location.reload();
    } catch (error) {
        // Error already handled in apiCall
    }
}

// ===================================
// RELATIONSHIP CRUD OPERATIONS
// ===================================

function openCreateRelationshipModal() {
    document.getElementById('relationshipId').value = '';
    document.getElementById('relationshipForm').reset();
    document.getElementById('relationshipModalTitle').textContent = 'Create New Relationship';
    document.getElementById('relationshipModal').style.display = 'block';
}

function editRelationship(relationshipId) {
    document.getElementById('relationshipId').value = relationshipId;
    document.getElementById('relationshipModalTitle').textContent = 'Edit Relationship';
    document.getElementById('relationshipModal').style.display = 'block';
    // TODO: Fetch and populate relationship data
}

function closeRelationshipModal() {
    document.getElementById('relationshipModal').style.display = 'none';
}

document.getElementById('relationshipForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = {
        gang_1_id: parseInt(document.getElementById('relationshipGang1').value),
        gang_2_id: parseInt(document.getElementById('relationshipGang2').value),
        relationship_type: document.getElementById('relationshipType').value,
        notes: document.getElementById('relationshipNotes').value
    };
    
    const relationshipId = document.getElementById('relationshipId').value;
    
    try {
        if (relationshipId) {
            await apiCall(`/api/relationship/${relationshipId}/update/`, 'POST', formData);
            alert('Relationship updated successfully!');
        } else {
            await apiCall('/api/relationship/create/', 'POST', formData);
            alert('Relationship created successfully!');
        }
        closeRelationshipModal();
        location.reload();
    } catch (error) {
        // Error already handled in apiCall
    }
});

async function deleteRelationship(relationshipId) {
    if (!confirm('Are you sure you want to delete this relationship? This action cannot be undone.')) {
        return;
    }
    
    try {
        await apiCall(`/api/relationship/${relationshipId}/delete/`, 'POST', {});
        alert('Relationship deleted successfully!');
        location.reload();
    } catch (error) {
        // Error already handled in apiCall
    }
}

// Close modals when clicking outside
window.onclick = function(event) {
    const modals = ['gangModal', 'memberModal', 'incidentModal', 'caseModal', 'relationshipModal'];
    modals.forEach(modalId => {
        const modal = document.getElementById(modalId);
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });
    
    // Handle image modal separately (closes on background click)
    const imageModal = document.getElementById('imageModal');
    if (imageModal && event.target == imageModal) {
        closeImageModal();
    }
}

