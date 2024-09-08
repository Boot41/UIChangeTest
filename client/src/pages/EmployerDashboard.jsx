import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import JobPostingForm from '../components/JobPostingForm';
import JobListingManager from '../components/JobListingManager';

const EmployerDashboard = () => {
  return (
    <div style={{ backgroundColor: '#F5F5F5', fontFamily: '"Roboto", sans-serif' }}>
      <Header />
      
      <div style={{ maxWidth: '80%', margin: '0 auto', padding: '24px', backgroundColor: '#FFFFFF', boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)', borderRadius: '4px' }}>
        <h1 style={{ color: '#212121', fontSize: '24px', fontWeight: '700', lineHeight: '1.5', marginBottom: '24px' }}>Employer Dashboard</h1>
        
        <section style={{ marginBottom: '24px' }}>
          <h2 style={{ color: '#212121', fontSize: '20px', fontWeight: '700', marginBottom: '16px' }}>Post a Job</h2>
          <JobPostingForm />
        </section>
        
        <section>
          <h2 style={{ color: '#212121', fontSize: '20px', fontWeight: '700', marginBottom: '16px' }}>Manage Job Listings</h2>
          <JobListingManager />
        </section>
      </div>

      <Footer />
    </div>
  );
};

export default EmployerDashboard;