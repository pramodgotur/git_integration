import React, { Component } from "react";
import axios from "axios";
import DataTable, { createTheme } from "react-data-table-component";

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
  };

  async componentDidMount() {
    const { perPage } = this.state;

    this.setState({ loading: true });

    const response = await axios.get(`/api/issues/?page=1&per_page=${perPage}&delay=1`);
    this.setState({
      data: response.data.results,
      totalRows: response.data.total,
      loading: false,
    });
  }

  handlePageChange = async (page) => {
    const { perPage } = this.state;

    this.setState({ loading: true });

    const response = await axios.get(`/api/issues/?page=${page}&page_size=${perPage}`);

    this.setState({
      loading: false,
      data: response.data.results,
    });
  };

  handlePerRowsChange = async (perPage, page) => {
    this.setState({ loading: true });

    const response = await axios.get(`/api/issues/?page=${page}&page_size=${perPage}`);

    this.setState({
      loading: false,
      data: response.data.results,
      perPage,
    });
  };

  render() {
    const { loading, data, totalRows } = this.state;

    return (
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
    );
  }
}

export default AdvancedPaginationTable;
