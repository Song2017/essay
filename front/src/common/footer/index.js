import React, { Component } from "react";
import { FooterWrapper } from "./style";

class Footer extends Component {
  render() {
    return <FooterWrapper onClick={()=>{window.location.href="https://baidu.com"}}> © 2019 - 沪ICP备19023181号-1 </FooterWrapper>;
  }
}

export default Footer;
