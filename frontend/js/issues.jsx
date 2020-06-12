import React, { Component } from "react";
import axios from "axios";
import DataTable, { createTheme } from "react-data-table-component";

import Select from "react-select";

const columns = [
  { name: "title", selector: "title" },
  { name: "state", selector: "state" },
  { name: "issue_number", selector: "issue_number" },
  { name: "issue_created_at", selector: "issue_created_at" },
];

class AdvancedPaginationTable extends Component {
  state = {
    data: [],
    loading: false,
    totalRows: 0,
    perPage: 10,
    selectedOptionLabel: null,
    labels: [],
    selectedOptionAssignee: null,
    assignees: [],
  };

  getAPIEndpoint(perPage, selectedOptionLabel, selectedOptionAssignee) {
    let api_endpoint;
    if (
      selectedOptionLabel != null &&
      selectedOptionLabel != undefined &&
      selectedOptionAssignee != null &&
      selectedOptionAssignee != undefined
    ) {
      api_endpoint = `/api/issues/?page=1&per_page=${perPage}&label=${selectedOptionLabel.value}&assignee=${selectedOptionAssignee.value}`;
    } else if (selectedOptionLabel != null && selectedOptionLabel != undefined) {
      api_endpoint = `/api/issues/?page=1&per_page=${perPage}&label=${selectedOptionLabel.value}`;
    } else if (selectedOptionAssignee != null && selectedOptionAssignee != undefined) {
      api_endpoint = `/api/issues/?page=1&per_page=${perPage}&assignee=${selectedOptionAssignee.value}`;
    } else {
      api_endpoint = `/api/issues/?page=1&per_page=${perPage}`;
    }
    return api_endpoint;
  }

  async componentDidMount() {
    const { perPage, selectedOptionLabel, selectedOptionAssignee } = this.state;
    this.setState({ loading: true });
    let api_endpoint = this.getAPIEndpoint(perPage, selectedOptionLabel, selectedOptionAssignee);

    const response = await axios.get(api_endpoint);
    this.setState({
      data: response.data.results,
      totalRows: response.data.total,
      loading: false,
    });

    this.getSelectOptionsforLabels();
    this.getSelectOptionsforAssignees();
  }

  handlePageChange = async (page) => {
    const { perPage, selectedOptionLabel } = this.state;

    this.setState({ loading: true });

    const response = await axios.get(`/api/issues/?page=${page}&page_size=${perPage}`);

    // let api_endpoint = this.getAPIEndpoint(perPage, selectedOptionLabel);
    // const response = await axios.get(api_endpoint);
    this.setState({
      loading: false,
      data: response.data.results,
    });
  };

  handlePerRowsChange = async (perPage, page) => {
    const { selectedOptionLabel } = this.state;
    this.setState({ loading: true });

    const response = await axios.get(`/api/issues/?page=${page}&page_size=${perPage}`);
    // let api_endpoint = this.getAPIEndpoint(perPage, selectedOptionLabel);
    // const response = await axios.get(api_endpoint);
    this.setState({
      loading: false,
      data: response.data.results,
      perPage,
    });
  };

  handleChangeLabel = async (selectedOptionLabel) => {
    this.setState({ selectedOptionLabel });
    console.log(`Option selected:`, selectedOptionLabel);
    const { perPage, selectedOptionAssignee } = this.state;
    let api_endpoint = this.getAPIEndpoint(perPage, selectedOptionLabel, selectedOptionAssignee);
    console.log("api_endpoint in label change", api_endpoint);
    this.setState({ loading: true });
    const response = await axios.get(api_endpoint);
    this.setState({
      loading: false,
      data: response.data.results,
      totalRows: response.data.total,
      perPage,
    });
  };

  handleChangeAssignee = async (selectedOptionAssignee) => {
    this.setState({ selectedOptionAssignee });
    console.log(`Option selected:`, selectedOptionAssignee);
    const { perPage, selectedOptionLabel } = this.state;
    let api_endpoint = this.getAPIEndpoint(perPage, selectedOptionLabel, selectedOptionAssignee);
    console.log("api_endpoint in assignee change", api_endpoint);
    this.setState({ loading: true });
    const response = await axios.get(api_endpoint);
    this.setState({
      loading: false,
      data: response.data.results,
      totalRows: response.data.total,
      perPage,
    });
  };

  async getSelectOptionsforLabels() {
    const response = await axios.get("/api/labels/");
    const labels_data = response.data.data;
    const labels = labels_data.map((info) => ({
      label: info.name,
      value: info.id,
    }));
    this.setState({ labels: labels });
  }

  async getSelectOptionsforAssignees() {
    const response = await axios.get("/api/assignees/");
    const assignees_data = response.data.data;
    const assignees = assignees_data.map((info) => ({
      label: info.login_name,
      value: info.id,
    }));
    this.setState({ assignees: assignees });
  }

  render() {
    console.log("render....called.....");

    const { loading, data, totalRows } = this.state;
    const { selectedOptionLabel } = this.state;
    const { labels } = this.state;
    const { assignees } = this.state;
    const { selectedOptionAssignee } = this.state;

    return (
      <div>
        <Select
          value={selectedOptionLabel}
          onChange={this.handleChangeLabel}
          options={labels}
          placeholder="Select Labels"
        />
        <br></br>
        <Select
          value={selectedOptionAssignee}
          onChange={this.handleChangeAssignee}
          options={assignees}
          placeholder="Select Assignee"
        />
        <br></br>
        <DataTable
          title="Github Issues"
          columns={columns}
          data={data}
          progressPending={loading}
          pagination
          paginationServer
          paginationTotalRows={totalRows}
          onChangeRowsPerPage={this.handlePerRowsChange}
          onChangePage={this.handlePageChange}
        />
      </div>
    );
  }
}

export default AdvancedPaginationTable;
