import React, { useState } from 'react';

interface Props {
  role: string;
  response: string;
  model: string;
  onModelChange: (model: string) => void;
}

const WorkshopMember: React.FC<Props> = ({ role, response, model, onModelChange }) => {
  const models = ['gpt-4-turbo', 'GPT-4', 'gpt-3.5-turbo', 'mistral-small', 'mistral-medium', 'mistral-large-latest', 'gemini-pro-1.5', 'gemini-pro', 'claude-3-haiku-20240307', 'claude-3-sonnet-20240229', 'claude-3-opus-20240229'];
  const [expanded, setExpanded] = useState(false);

  const handleClick = () => {
    setExpanded(!expanded);
  };

  return (
    <div className={`workshop-member ${expanded ? 'expanded' : ''}`}>
      <div className="label-instruction-container">
        <label>{role}</label>
        <p className="click-instruction">Click review text to expand</p>
      </div>
      <select value={model} onChange={(e) => onModelChange(e.target.value)}>
        {models.map((m) => (
          <option key={m} value={m}>
            {m}
          </option>
        ))}
      </select>
      <textarea value={response} readOnly onClick={handleClick} />
    </div>
  );
};

export default WorkshopMember;