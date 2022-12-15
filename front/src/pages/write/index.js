import React, { PureComponent } from "react";
import { Redirect } from "react-router-dom";
import { connect } from "react-redux";
import { Button, Input } from "./style";
import { actionCreators } from "./store";
import MDEditor from "@uiw/react-md-editor";

class Write extends PureComponent {
  render() {
    const { loginStatus, content, title, save, saveEditor } = this.props;
    if (loginStatus) {
      return (
        <div>
          <div>
            Title
            <Input
              placeholder={title}
              ref={(input) => {
                this.title = input;
              }}
            />
            <Button onClick={() => save(this.title, content)}>保存</Button>
          </div>
          <div className="container">
            <MDEditor value={content} onChange={saveEditor} />
            <MDEditor.Markdown
              source={content}
              style={{ whiteSpace: "pre-wrap" }}
            />
          </div>
        </div>
      );
    } else {
      return <Redirect to="/login" />;
    }
  }
}

const mapState = (state) => ({
  loginStatus: state.getIn(["login", "login"]),
  content: state.getIn(["aritle", "articleData"]),
  title: state.getIn(["aritle", "title"]),
});

const mapDispatch = (dispatch) => ({
  save(titleEle, contentEle) {
    dispatch(actionCreators.save(titleEle.value, contentEle));
  },
  saveEditor(contentEle) {
    dispatch(actionCreators.saveEditor(contentEle));
  },
});
export default connect(mapState, mapDispatch)(Write);
