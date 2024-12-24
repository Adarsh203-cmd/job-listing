import React from 'react';

const JobCard = ({ job }) => {
  return (
    <div className="border p-4 rounded-lg shadow-sm hover:shadow-lg transition bg-white">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-semibold text-gray-800">{job.title}</h2>
        {job.job_type && (
          <span className="bg-blue-100 text-blue-700 text-sm px-3 py-1 rounded-full">
            {job.job_type}
          </span>
        )}
      </div>
      <p className="text-gray-600 mt-2">{job.company}</p>
      <p className="text-gray-500">{job.location}</p>
      <p className="text-sm text-green-600 mt-2">
        {job.salary || 'Salary not specified'}
      </p>
      <a
        href={job.details_url}
        target="_blank"
        rel="noopener noreferrer"
        className="text-blue-600 hover:underline mt-4 inline-block"
      >
        View Details
      </a>
    </div>
  );
};

export default JobCard;
