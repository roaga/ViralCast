import twitter from './twitter.png';
import virus from './virus.png';
import './App.css';
import { BsChevronDown } from "react-icons/bs";
import Iframe from 'react-iframe'
import React, {useState, useRef} from 'react';
import * as V from 'victory';
import {VictoryChart, VictoryBar, VictoryLine, VictoryTheme, VictoryLegend, VictoryAxis, VictoryPie} from 'victory';

function App() {
    const [tweet, setTweet] = useState("");
    const [followers, setFollowers] = useState(null);
    const [friends, setFriends] = useState(null);
    const [favorites, setFavorites] = useState(0);
    const [verified, setVerified] = useState(false);
    const [retweets, setRetweets] = useState(0);
    const [features, setFeatures] = useState(null);
    const myRef = useRef(null);

    const executeScroll = () => myRef.current.scrollIntoView({ behavior: 'smooth'});

    const handleTweet = (e) => {
        e.preventDefault();
        // extract features    
        fetch("http://localhost:5000/features/" + tweet.replace(" ", "-") + "/" + followers + "/" + friends + "/" + verified).then(res => res.json()).then(
            (result) => {
                setFeatures(result)

                // pass features into ML model
                fetch("http://localhost:5000/predict/" + JSON.stringify(result).replace(" ", "-")).then(res => res.json()).then(
                    (result) => {
                        setFavorites(Math.round(Math.abs(result['favorites']) / 20))
                        setRetweets(Math.round(Math.abs(result['retweets'])))
                    }
                )
            }
        );
    }

    return (
        <div className="App">
            <header className="App-header">
                <h1>ViralCast</h1>
                <h2 style={{fontWeight: "bold"}}>Predicting the Spread<br/>of COVID-19 Misinformation<br/>on Twitter</h2>

                <div style={{display: "flex", flexDirection: "row", justifyContent: "space-evenly", margin: 64}}>
                    <img src={virus} className="App-logo" alt="logo"  style={{width: 200, height: 200, marginRight: 64}}/>
                    <img src={twitter} className="App-logo" alt="logo" style={{width: 200, height: 200, marginLeft: 64}}/>
                </div>

                <BsChevronDown size={144} style={{marginBottom: 96}} onClick={executeScroll} className="scroll-down"/>

                <div style={{width: "100%"}}>
                    <h2 ref={myRef}>Visualizing Our Model</h2>
                    {/* <Iframe url="https://google.com"
                        width="90%"
                        height="1000px"
                        id="myId"
                        className="myClassname"
                        display="initial"
                        position="relative"
                    /> */}
                    <h3>R-squared values for Models Predicting...</h3>
                    <div style={{display: "flex", flexDirection: "row", justifyContent: "space-evenly", marginTop: 0}}>
                        <h3 style={{color: "#e7505f"}}>Favorites</h3>
                        <h3 style={{color: "#61dafb"}}>Retweets</h3>
                    </div>
                    <div style={{display: "flex", flexDirection: "row", justifyContent: "space-evenly", marginTop: 0}}>
                        <VictoryPie
                            standalone={true}
                            width={300} height={300}
                            animate={{duration: 2000, onLoad: { duration: 1000 }}} 
                            innerRadius={48}
                            cornerRadius={10}
                            data={[{x: "0.95", y: 0.95}, {x: " ", y: 0.05}]}
                            colorScale={["#e7505f", "white"]}
                        />
                        <VictoryPie
                            standalone={true}
                            width={300} height={300}
                            animate={{duration: 2000, onLoad: { duration: 1000 }}} 
                            innerRadius={48}
                            cornerRadius={10}
                            data={[{x: "0.92", y: 0.92}, {x: " ", y: 0.05}]}
                            colorScale={["#61dafb", "white"]}
                        />
                    </div>
                </div>

                <div style={{width: "100%"}}>
                    <h2>Try It Yourself</h2>

                    <div style={{display: "flex", flexDirection: "row", justifyContent: "space-evenly", margin: 64}}>
                        <form onSubmit={(e) => handleTweet(e)} style={{display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center"}}>
                            <h3>Test a Tweet</h3>
                            <textarea value={tweet} onChange={event => setTweet(event.target.value)} maxLength={280} placeholder="Write your tweet here."/>
                            <textarea type="number" value={followers} onChange={event => setFollowers(event.target.value.replace(/\D/g,''))} style={{height: 30}} maxLength={10} placeholder="How many followers do you have?"/>
                            <textarea type="number" value={friends} onChange={event => setFriends(event.target.value.replace(/\D/g,''))} style={{height: 30}} maxLength={10} placeholder="How many do you follow back?"/>
                            <div style={{flexDirection: "row", display: "flex", alignItems: "center"}}>
                                <input type="checkbox" value={"Verified?"} id="verified" onChange={() => setVerified(!verified)}/>
                                <h6 style={{marginLeft: 16}}>Verified?</h6>
                            </div>
        
                            <input type="submit" value={"Predict Spread"}/>
                        </form>

                        <VictoryChart theme={VictoryTheme.material} domainPadding={{x: 100}} categories={{x: ["Favorites", "Retweets"]}} domain={{y: [0, 1000]}}>
                            <VictoryBar
                                style={{ data: {fill: ({ datum }) => datum.x === "Favorites" ? "#e7505f" : "#61dafb"}}}
                                barRatio={0.5}
                                cornerRadius={{top: 14}}
                                animate={{duration: 2000, onLoad: { duration: 1000 }}} 
                                data={[
                                    {x: "Favorites", y: favorites},
                                    {x: "Retweets", y: retweets},
                                ]}
                            />
                        </VictoryChart>

                        <div>
                            <h3>Prediction</h3>
                            <h5>Favorites:<br/> {favorites}</h5>
                            <h5>Retweets:<br/> {retweets}</h5>
                        </div>
                    </div>
                </div>

                <h2>About the Project</h2>
                <h5 style={{lineHeight: 2}}>
                    Using a <a href="https://www.kaggle.com/smid80/coronavirus-covid19-tweets-late-april" target="_blank">dataset</a> of 500k tweets about COVID-19,
                    <br/>
                    we trained a model to predict how far a tweet would spread<br/>based on properties of its language,<br/>including sentiment, emotion, and entity analysis.
                </h5>
                <h5 style={{lineHeight: 2}}>
                    We used IBM Watson Natural Language Understanding for text analysis
                    <br/>
                    and regression in SciKit-Learn for machine learning.
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
