import React, {Component} from 'react';
import {Person} from './schema/models/Person';
import {GenderEnum} from './schema/models/GenderEnum';
import {ApiApi} from './schema/apis/ApiApi';
import {Configuration} from './schema/runtime';

function renderGender(gender: GenderEnum): string {
  switch (gender) {
    case GenderEnum.M: return 'Male';
    case GenderEnum.F: return 'Female';
    case GenderEnum.X: return 'Other';
  }
}

interface PersonViewState {
  data: Person | null
}

export class PersonView extends Component<{}, PersonViewState> {

  constructor(props: {}) {
    super(props);
    this.state = {data: null};
  }

  fetchData() {
    const apiConf = new Configuration({
      basePath: 'http://127.0.0.1:8000'
    });
    const api = new ApiApi(apiConf);
    api.apiPersonRetrieve({id: 1})
    .then(
      person => {
        this.setState({data: person});
      }
    )
  }

  componentDidMount() {
    this.fetchData();
  }

  render() {
    if (this.state.data == null) {
      return <div>Loading…</div>
    } else {
      return <table><tbody>
        <tr><td>First name</td><td>{this.state.data.firstName}</td></tr>
        <tr><td>Last name</td><td>{this.state.data.lastName}</td></tr>
        <tr><td>Birthdate</td><td>{this.state.data.birthdate.toString()}</td></tr>
        <tr><td>Gender</td><td>{renderGender(this.state.data.gender)}</td></tr>
        </tbody></table>
    }
  }
}
