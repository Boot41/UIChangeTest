import React, { useState } from 'react';

const JobPostingForm = ({ onSubmit }) => {
  const [jobTitle, setJobTitle] = useState('');
  const [jobDescription, setJobDescription] = useState('');
  const [qualifications, setQualifications] = useState('');
  const [location, setLocation] = useState('');
  const [jobType, setJobType] = useState('');
  const [deadline, setDeadline] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const jobData = { jobTitle, jobDescription, qualifications, location, jobType, deadline };
    onSubmit(jobData);
    // Reset form
    setJobTitle('');
    setJobDescription('');
    setQualifications('');
    setLocation('');
    setJobType('');
    setDeadline('');
  };

  return (
    <form onSubmit={handleSubmit} style={{ backgroundColor: '#FFFFFF', padding: '16px', borderRadius: '4px', boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)', maxWidth: '80%', margin: 'auto' }}>
      <h2 style={{ fontFamily: '"Roboto", sans-serif', fontSize: '24px', color: '#212121', marginBottom: '16px' }}>Job Posting Form</h2>
      
      <label style={{ display: 'block', marginBottom: '8px', color: '#212121', fontWeight: '700' }}>Job Title</label>
      <input type="text" value={jobTitle} onChange={(e) => setJobTitle(e.target.value)} required style={{ width: '100%', padding: '8px', border: '1px solid #E0E0E0', borderRadius: '4px', marginBottom: '16px' }} />
      
      <label style={{ display: 'block', marginBottom: '8px', color: '#212121', fontWeight: '700' }}>Description</label>
      <textarea value={jobDescription} onChange={(e) => setJobDescription(e.target.value)} required style={{ width: '100%', padding: '8px', border: '1px solid #E0E0E0', borderRadius: '4px', marginBottom: '16px' }} />
      
      <label style={{ display: 'block', marginBottom: '8px', color: '#212121', fontWeight: '700' }}>Qualifications</label>
      <input type="text" value={qualifications} onChange={(e) => setQualifications(e.target.value)} required style={{ width: '100%', padding: '8px', border: '1px solid #E0E0E0', borderRadius: '4px', marginBottom: '16px' }} />
      
      <label style={{ display: 'block', marginBottom: '8px', color: '#212121', fontWeight: '700' }}>Location</label>
      <input type="text" value={location} onChange={(e) => setLocation(e.target.value)} required style={{ width: '100%', padding: '8px', border: '1px solid #E0E0E0', borderRadius: '4px', marginBottom: '16px' }} />
      
      <label style={{ display: 'block', marginBottom: '8px', color: '#212121', fontWeight: '700' }}>Job Type</label>
      <select value={jobType} onChange={(e) => setJobType(e.target.value)} required style={{ width: '100%', padding: '8px', border: '1px solid #E0E0E0', borderRadius: '4px', marginBottom: '16px' }}>
        <option value="" disabled>Select job type</option>
        <option value="full-time">Full-time</option>
        <option value="part-time">Part-time</option>
        <option value="contract">Contract</option>
      </select>
      
      <label style={{ display: 'block', marginBottom: '8px', color: '#212121', fontWeight: '700' }}>Application Deadline</label>
      <input type="date" value={deadline} onChange={(e) => setDeadline(e.target.value)} required style={{ width: '100%', padding: '8px', border: '1px solid #E0E0E0', borderRadius: '4px', marginBottom: '16px' }} />
      
      <button type="submit" style={{ backgroundColor: '#4CAF50', color: '#FFFFFF', padding: '10px 20px', border: 'none', borderRadius: '4px', cursor: 'pointer', transition: '0.3s ease-in-out' }}>
        Submit Job Posting
      </button>
    </form>
  );
};

export default JobPostingForm;