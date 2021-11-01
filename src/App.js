import React, { useState } from "react";
import { KATHAS_BY_ANG } from "./kathasByAng";
import { KATHAS_BY_KEYWORD } from "./kathasByKeyword";

//'npm run deploy' before push
function App() {
  const [angMessage, setAngMessage] = useState("");
  const [keyWordMessage, setKeyWordMessage] = useState("");
  const [ang, setAng] = useState("");
  const [keyword, setKeyword] = useState("");

  function randId() {
    return Math.random().toString(36).substr(2, 9);
  }
  function kathaForAng(angNum) {
    function SantGianiGurbachanJiKatha() {
      let a;
      try {
        a = KATHAS_BY_ANG["SantGianiGurbachanSinghJi"][angNum].map((katha) => {
          return (
            <div key={randId()}>
              <h3>{katha.title}</h3>
              <ol>
                {katha.links.map((link) => {
                  return (
                    <li key={randId()}>
                      <a href={link} target="_blank" rel="noopener noreferrer">
                        {link}
                      </a>

                      <video width="500" height="60" controls name="media">
                        <source src={link} type="audio/mpeg" />
                      </video>
                    </li>
                  );
                })}
              </ol>
              {/* <div>
                <a href={i} target="_blank" rel="noopener noreferrer">
                  {i.title}
                </a>
              </div>
              <video width="500" height="60" controls name="media">
                <source src={i} type="audio/mpeg" />
              </video> */}
            </div>
          );
        });
      } catch (e) {
        a =
          ".....No ਕਥਾ for ang " +
          angNum +
          " from Sant Giani Gurbachan Singh Ji";
      }
      return a;
    }
    function GianiSherJiKatha() {
      let a;
      try {
        a = KATHAS_BY_ANG["GianiSherSinghJi"][angNum].map((katha) => {
          return (
            <div key={randId()}>
              <h3>{katha.title}</h3>
              <ol>
                {katha.links.map((link) => {
                  return (
                    <li key={randId()}>
                      <a href={link} target="_blank" rel="noopener noreferrer">
                        {link}
                      </a>

                      <video width="500" height="60" controls name="media">
                        <source src={link} type="audio/mpeg" />
                      </video>
                    </li>
                  );
                })}
              </ol>
            </div>
          );
        });
      } catch (e) {
        a = "";
      }
      return a;
    }
    return (
      <div>
        <h1>Sant Giani Gurbachan Singh Ji Katha</h1>
        {SantGianiGurbachanJiKatha()}
        {GianiSherJiKatha() === "" ? (
          ""
        ) : (
          <div>
            <h1>Giani Sher Singh Ji Katha</h1>
            {GianiSherJiKatha()}
          </div>
        )}
      </div>
    );
  }

  function kathaForKeyword(word) {
    if (word === "") {
      return <div>Please enter a keyword</div>;
    }
    const lstOfKeys = Object.keys(KATHAS_BY_KEYWORD);

    let a;
    let ans = [];

    try {
      a = lstOfKeys.map((kathaTitle) => {
        if (kathaTitle.toLowerCase().includes(word.toLowerCase())) {
          let eachLink = kathaTitle;
          let theLinks = KATHAS_BY_KEYWORD[kathaTitle].links.map((link) => {
            return (
              <li key={randId()}>
                <a href={link} target="_blank" rel="noopener noreferrer">
                  {link}
                </a>

                <video width="500" height="60" controls name="media">
                  <source src={link} type="audio/mpeg" />
                </video>
              </li>
            );
          });
          ans.push(
            <li key={randId()}>
              <h3>{eachLink}</h3>
              <ol>{theLinks}</ol>
            </li>
          );
        }
      });
    } catch (e) {
      console.log(e);
      a = <div>Not valid evtry</div>;
    }
    return ans;
  }

  return (
    <div>
      <div>Sant Giani Gurbachan Singh Ji Bhindran Wale ਕਥਾ</div>
      <div>Enter the Ang Number for which you want ਕਥਾ of:</div>
      <h3>
        ਉਹ ਅੰਗ ਨੰਬਰ ਦਰਜ ਕਰੋ ਜਿਸ ਲਈ ਤੁਸੀਂ ਸੰਤ ਗਿਆਨੀ ਗੁਰਬਚਨ ਸਿੰਘ ਜੀ ਭਿੰਡਰਾਵਾਲੇ
        ਦੁਆਰਾ ਕਥਾ ਸੁਣਨਾ ਚਾਹੁੰਦੇ ਹੋ:
      </h3>
      <div>
        <form onSubmit={(e) => e.preventDefault()}>
          <input
            autoFocus="autofocus"
            type="number"
            placeholder="ex: 1084"
            value={ang}
            onChange={(event) => {
              setAng(event.target.value);
            }}
          />
          <button
            type="submit"
            onClick={() => {
              if (0 < ang && ang < 1431) {
                setAngMessage(() => {
                  let theKhata = kathaForAng(ang);
                  return theKhata;
                });
              } else {
                alert("Please enter vallid ang number");
              }
            }}
          >
            Submit
          </button>
        </form>
        <button
          onClick={() => {
            const getRandomAng = () => Math.floor(Math.random() * 1430) + 1;
            const a = getRandomAng();
            setAng(a);
            setAngMessage(() => {
              let theKhata = kathaForAng(a);
              return theKhata ? theKhata : "....No Khatas Yet";
            });
          }}
        >
          random ang
        </button>
        <div>{angMessage}</div>
        <br />
        <br />
        <br />
        <br />
        <hr />
        <div>Enter the keyword for which you want ਕਥਾ of:</div>
        <h3>
          ਉਹ ਸ਼ਬਦ ਦਰਜ ਕਰੋ ਜਿਸ ਲਈ ਤੁਸੀਂ ਸੰਤ ਗਿਆਨੀ ਗੁਰਬਚਨ ਸਿੰਘ ਜੀ ਭਿੰਡਰਾਵਾਲੇ ਦੁਆਰਾ
          ਕਥਾ ਸੁਣਨਾ ਚਾਹੁੰਦੇ ਹੋ:
        </h3>
        <form onSubmit={(e) => e.preventDefault()}>
          <input
            autoFocus="autofocus"
            type="text"
            placeholder="ex: sukhmani"
            value={keyword}
            onChange={(event) => {
              setKeyword(event.target.value);
            }}
          />
          <button
            type="submit"
            onClick={() => {
              if (keyword.split(" ").length === 1) {
                setKeyWordMessage(() => {
                  let theKhata = kathaForKeyword(keyword);
                  if (theKhata.length === 0) {
                    return "No katha titles with '" + keyword + "' in it";
                  }
                  return <ol>{theKhata}</ol>;
                });
              } else {
                alert("Please enter only 1 word");
              }
            }}
          >
            Submit
          </button>
        </form>
        <button
          onClick={() => {
            const getRandomKeyWord = () =>
              Object.keys(KATHAS_BY_KEYWORD)[
                Math.floor(
                  Math.random() * Object.keys(KATHAS_BY_KEYWORD).length
                ) + 1
              ];
            const a = getRandomKeyWord();
            setKeyword(a);
            setKeyWordMessage(() => {
              let theKhata = kathaForKeyword(a);
              return theKhata ? theKhata : "....No Khatas Yet";
            });
          }}
        >
          random ang
        </button>
        <div>{keyWordMessage}</div>
      </div>
    </div>
  );
}

export default App;
