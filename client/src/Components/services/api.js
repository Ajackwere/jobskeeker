import axios from 'axios';

const API_BASE_URL = 'https://jobseekerhub.onrender.com/';

const api = axios.create({
    baseURL: API_BASE_URL,
});

export const jobApi = {
    getAllJobs: () => api.get('/api/jobs/'),
    getJobById: (id) => api.get('/api/jobs/${id}/'),
    postNewJob: () => api.post('/api/jobs'),
    applyToJob: (jobId, data) => api.post('/api/jobs/${jobId}/apply', data),
    deleteJob: () => api.delete('/api/jobs/${id}/'),
    updateJob: () => api.put('/api/jobs/${id}/'),
    partiallyUpdateJob: () => api.patch('/api/jobs/${id}/'),


    viewApplications: () => api.get('/api/applications/'),
    viewMyApplications: () => api.get('/api/applications/my_applications/'),
    viewApplicationById: (id) => api.get('/api/applications/${id}/'),
    updateApplicationStatus: (id) => api.put('/api/applications/${id}/'),
    partiallyUpdateApplicationStatus: (id) => api.patch('api/applications/${id}/'),
    deleteApplication: (id) => api.delete('/api/applications/${id}/'),

    getAllEmployers: () => api.get('/api/employers/'),
    createNewEmployer: () => api.post('/api/employers/'),
    getEmployerById: () => api.get('/api/employers/${id}/'),
    updateEmployer: () => api.put('/api/employers/${id}/'),
    partiallyUpdateEmployer: () => api.patch('/api/employers/${id}/'),
    deleteEmployer: () => api.delete('/api/employers/${id}/'),

    viewMyApplicants: () => api.get('/api/jobs/${id}/my_applicants/'),
    getAllJobSeekers: () => api.get('/api/jobseekers/'),
    postJobSeekers: () => api.get('/api/jobseekers/'),
    getJobSeekerById: () => api.get('/api/jobseekers/${id}/'),

};

export default api;
