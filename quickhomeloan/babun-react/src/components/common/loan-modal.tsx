import React, { useState, useEffect } from 'react';
import axios from 'axios';

const LoanModal: React.FC = () => {
    const [csrfToken, setCsrfToken] = useState('');
    const [requiredAmount, setRequiredAmount] = useState('');
    const [needTime, setNeedTime] = useState('');
    const [bankType, setBankType] = useState('');
    const [name, setName] = useState('');
    const [mobile, setMobile] = useState('');
    const [successMessage, setSuccessMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    // Fetch CSRF token from Django on component mount
    useEffect(() => {
        const fetchCsrfToken = async () => {
            try {
                const response = await axios.get('http://54.158.143.81/api/get-csrf-token/');
                setCsrfToken(response.data.csrfToken);
            } catch (error) {
                console.error('Error fetching CSRF token:', error);
            }
        };

        fetchCsrfToken();
    }, []);

    // Handle form submission
    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();

        const formData = {
            required_amount: requiredAmount,
            need_time: needTime,
            bank_type: bankType,
            name: name,
            mobile: mobile,
        };

        try {
            const response = await axios.post('http://54.158.143.81/api/loan-application/', formData, {
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken || '',  // Add CSRF token to headers
                }
            });

            if (response.status === 201) {
                setSuccessMessage('Loan application submitted successfully!');
                setErrorMessage('');
            }
        } catch (error: unknown) {  // Specify the error type as 'unknown'
            if (axios.isAxiosError(error)) {  // Type guard for AxiosError
                setErrorMessage('Failed to submit the application. Please try again.');
                setSuccessMessage('');
            } else {
                console.error('An unexpected error occurred:', error);
            }
        }
    };

    return (
        <div className="modal fade" id="loanModal" tabIndex={-1} aria-labelledby="loanModalLabel" aria-hidden="true">
            <div className="modal-dialog">
                <div className="modal-content">
                    <div className="modal-header">
                        <h5 className="modal-title" id="loanModalLabel">Apply for Home Loan</h5>
                        <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div className="modal-body">
                        <form onSubmit={handleSubmit}>
                            <div className="mb-3">
                                <label htmlFor="requiredAmount" className="form-label">Required Amount</label>
                                <input
                                    type="text"
                                    className="form-control"
                                    id="requiredAmount"
                                    value={requiredAmount}
                                    onChange={(e) => setRequiredAmount(e.target.value)}
                                    required
                                />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="needTime" className="form-label">Time Needed (Months)</label>
                                <input
                                    type="text"
                                    className="form-control"
                                    id="needTime"
                                    value={needTime}
                                    onChange={(e) => setNeedTime(e.target.value)}
                                    required
                                />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="bankType" className="form-label">Bank Type</label>
                                <input
                                    type="text"
                                    className="form-control"
                                    id="bankType"
                                    value={bankType}
                                    onChange={(e) => setBankType(e.target.value)}
                                    required
                                />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="name" className="form-label">Your Name</label>
                                <input
                                    type="text"
                                    className="form-control"
                                    id="name"
                                    value={name}
                                    onChange={(e) => setName(e.target.value)}
                                    required
                                />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="mobile" className="form-label">Mobile Number</label>
                                <input
                                    type="text"
                                    className="form-control"
                                    id="mobile"
                                    value={mobile}
                                    onChange={(e) => setMobile(e.target.value)}
                                    required
                                />
                            </div>
                            <div className="mb-3">
                                <button type="submit" className="btn btn-primary">Submit</button>
                            </div>
                        </form>

                        {successMessage && <div className="alert alert-success">{successMessage}</div>}
                        {errorMessage && <div className="alert alert-danger">{errorMessage}</div>}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default LoanModal;
