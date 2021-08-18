import React, { useState } from "react";
import Dropdown from "./Dropdown";
import Convert from "./Convert";

const options = [
  {
    label: "Afrikaans",
    value: "af",
  },
  {
    label: "Japanese",
    value: "ja",
  },
  {
    label: "Chinese",
    value: "zh-TW",
  },
  {
    label: "Dutch",
    value: "nl",
  },
];

const Translate = () => {
  const [lang, setLang] = useState(options[0]);
  const [text, setText] = useState("");

  return (
    <div>
      <div className="ui form">
        <div className="field">
          <label>Enter text</label>
          <input
            value={text}
            onChange={(e) => {
              setText(e.target.value);
            }}
          />
        </div>
      </div>
      <Dropdown
        options={options}
        selected={lang}
        onSelectedChange={setLang}
        label="Select a Language"
      />
      <hr />
      <h3 className="ui header">Output</h3>
      <Convert text={text} language={lang} />
    </div>
  );
};

export default Translate;
