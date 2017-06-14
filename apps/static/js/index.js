var React = require('react')
var ReactDOM = require('react-dom')
var BooksList = require('./books-list')

ReactDOM.render(<BooksList url='/api/' pollInterval={1000}/>, document.getElementById('container'))