import twitter from './twitter.png';
import virus from './virus.png';
import './App.css';
import { BsChevronDown } from "react-icons/bs";
import Iframe from 'react-iframe'
import React, {useState, useEffect} from 'react';

function App() {
    const [tweet, setTweet] = useState("");
    const [favorites, setFavorites] = useState(0);
    const [retweets, setRetweets] = useState(0);

    const handleTweet = () => {
        // TODO: call our ML model for predictions and set favorites and retweets

    }

    return (
        <div className="App">
            <header className="App-header">
                <h1 style={{fontWeight: "bold"}}>Predicting the Spread<br/>of COVID-19 Misinformation<br/>on Twitter</h1>

                <div style={{display: "flex", flexDirection: "row", justifyContent: "space-evenly", margin: 64}}>
                    <img src={virus} className="App-logo" alt="logo"  style={{width: 200, height: 200, marginRight: 64}}/>
                    <img src={twitter} className="App-logo" alt="logo" style={{width: 200, height: 200, marginLeft: 64}}/>
                </div>

                <BsChevronDown size={144} style={{marginBottom: 96}}/>

                <div style={{width: "100%"}}>
                    <h2>Visualizing Our Model</h2>
                    <Iframe url="http://www.youtube.com/embed/xDMP3i36naA"
                        width="90%"
                        height="1000px"
                        id="myId"
                        className="myClassname"
                        display="initial"
                        position="relative"
                    />
                </div>

                <div style={{width: "100%"}}>
                    <h2>Try It Yourself</h2>

                    <div style={{display: "flex", flexDirection: "row", justifyContent: "space-evenly", margin: 64}}>
                        <form onSubmit={(e) => handleTweet(e)} style={{display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center"}}>
                            <h3>Write a Tweet</h3>
                            <textarea value={tweet} onChange={event => setTweet(event.target.value)} maxLength={280}/>
                            <input type="submit" value={"Predict Spread"}/>
                        </form>

                        <div>
                            <h3>Prediction</h3>
                            <h5>Favorites: {favorites}</h5>
                            <h5>Retweets: {retweets}</h5>
                        </div>
                    </div>
                </div>

                <h2>About the Project</h2>
                <h5 style={{lineHeight: 2}}>
                    Using a <a href="https://www.kaggle.com/smid80/coronavirus-covid19-tweets-late-april" target="_blank">dataset</a> of [] tweets about COVID-19,
                    <br/>
                    we trained a model to predict how far a tweet would spread<br/>based on properties of its language.
                </h5>
                <h5 style={{lineHeight: 2}}>
                    We used Google Cloud NLP for text analysis
                    <br/>
                    and IBM Cognos Analytics for data visualization.
                    <br/>
                    This web app was built in React and Flask.
                    <br/>
                </h5>
                <h5 style={{lineHeight: 2}}>
                    Created @ HackRPI 2020.
                </h5>


                <h6>&copy;2020 Rohan Agarwal, Jed Magracia, Hanif Fauzan, Bao Tran</h6>
            </header>
        </div>
    );
}

export default App;
