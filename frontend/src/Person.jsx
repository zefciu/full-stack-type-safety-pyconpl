import React, {Component} from 'react';

const renderGender = (code) => {
  switch (code) {
    case 'M': return 'Male';
    case 'F': return 'Female';
    default: throw new Error('Unexpected value for gender');
  }
}

export class Person extends Component {

  constructor(props) {
    super(props);
    this.state = {data: null};
  }

  fetchData() {
    fetch('http://127.0.0.1:8000/api/person/1')
    .then(
      response => 
        response.json()
      )
    .then(
      data => {
        this.setState({data: data});
      }
    );
  }

  componentDidMount() {
    this.fetchData();
  }

  render() {
    if (this.state.data == null) {
      return <div>Loading…</div>
    } else {
      return <table><tbody>
        <tr><td>First name</td><td>{this.state.data.first_name}</td></tr>
        <tr><td>Last name</td><td>{this.state.data.last_name}</td></tr>
        <tr><td>Birthdate</td><td>{this.state.data.birthdate.toString()}</td></tr>
        <tr><td>Gender</td><td>{renderGender(this.state.data.gender)}</td></tr>
        </tbody></table>
    }
  }
}
