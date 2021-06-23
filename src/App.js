import { useState } from "react";
import { khata } from "./khata";

//'npm run deploy' before push
function App() {
  const [message, setMessage] = useState("");
  const [ang, setAng] = useState("");

  function khataForAng(angNum) {
    function randId() {
      return Math.random().toString(36).substr(2, 9);
    }
    function whatToReturn() {
      let a;
      try {
        a = khata[angNum].map((i) => {
          return (
            <li key={randId()}>
              <div>
                <a href={i} target="_blank" rel="noopener noreferrer">
                  {i}
                </a>
              </div>
              <video width="500" height="60" controls name="media">
                <source src={i} type="audio/mpeg" />
              </video>
            </li>
          );
        });
      } catch (e) {
        a = ".....No ਕਥਾ for ang " + angNum;
      }
      return a;
    }
    return <ol>{whatToReturn()}</ol>;
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
