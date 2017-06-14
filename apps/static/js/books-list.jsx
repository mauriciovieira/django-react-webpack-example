var React = require('react')

module.exports = React.createClass({
    loadBooksFromServer: function(){
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        })
    },

    getInitialState: function() {
        return {data: []};
    },

    componentDidMount: function() {
        this.loadBooksFromServer();
        setInterval(this.loadBooksFromServer,
                    this.props.pollInterval)
    },

    render: function() {
        if (this.state.data) {
            console.log('DATA!')
            var bookNodes = this.state.data.map(function(book){
                return <li> {book.title} - {book.author} </li>
            })
        }
        return (
            <div>
                <h1>Hello React!</h1>
                <ol>
                    {bookNodes}
                </ol>
            </div>
        )
    }
})