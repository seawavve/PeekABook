import React, { Component } from 'react';

class CreateContent extends Component {
  render() {
    return (
      <article>
        <h2>Create</h2>
        <form action="/create_process" method="post"
          onSubmit={function(e) {
            e.preventDefault();
            debugger;
            this.props.onSubmit(
              e.target.title.value,
              e.target.desc.value
            );
          }.bind(this)}
        >
          {/*여기가 텍스트 업로드*/}
          <p><input type="file" name="upload text file"></input></p>
          <p><input type="submit"></input></p>
          {/*<p><input type="text" name="title" placeholder="title"></input></p>
          <p>
            <textarea name="desc" placeholder="description"></textarea>
          </p>
          <p>
            <input type="submit"></input>
          </p>*/}
        </form>
      </article>
    );
  }
}

export default CreateContent;