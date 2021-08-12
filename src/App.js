import { useState } from "react";
import { KATHAS } from "./KATHAS";

//'npm run deploy' before push
function App() {
  const [message, setMessage] = useState("");
  const [ang, setAng] = useState("");

  function khataForAng(angNum) {
    function randId() {
      return Math.random().toString(36).substr(2, 9);
    }
    function SantGianiGurbachanJiKatha() {
      let a;
      try {
        a = KATHAS["SantGianiGurbachanSinghJi"][angNum].map((katha) => {
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
        a = KATHAS["GianiSherSinghJi"][angNum].map((katha) => {
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
        a = ".....No ਕਥਾ for ang " + angNum + " from Giani Sher Singh Ji";
      }
      return a;
    }
    return (
      <div>
        <h1>Sant Giani Gurbachan Singh Ji Katha</h1>
        {SantGianiGurbachanJiKatha()}
        <hr></hr>
        <h1>Giani Sher Singh Ji Katha</h1>
        {GianiSherJiKatha()}
      </div>
    );
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
                setMessage(() => {
                  let theKhata = khataForAng(ang);
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
        <div>{message}</div>
        <button
          onClick={() => {
            const getRandomAng = () => Math.floor(Math.random() * 1430) + 1;
            const a = getRandomAng();
            setAng(a);
            setMessage(() => {
              let theKhata = khataForAng(a);
              return theKhata ? theKhata : "....No Khatas Yet";
            });
          }}
        >
          random ang
        </button>
      </div>
    </div>
  );
}

export default App;
