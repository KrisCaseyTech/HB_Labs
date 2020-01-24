class Homepage extends React.Component {
	render(){
		return (
            <div>
                <p>Here are all of our Trading Cards!</p>
                <a href="/cards">Click here to view trading cards.</a>
                <img src="/static/img/balloonicorn.jpg" />
            </div>
        );
	}
}

ReactDOM.render(<Homepage />, document.getElementById('app'));