// Redux的核心概念：
//  Component 借书人
//  Action creators 借书人要做的操作 dispatch(action)
//  Store 图书管理员 (previpus state, action) <-> (new state)
//  Reducers 图书记录本
//  将需要修改的state都存入到store里，发起一个action用来描述发生了什么，用reducers描述action如何改变state tree 。
//  创建store的时候需要传入reducer，真正能改变store中数据的是store.dispatch API
import { createStore, compose, applyMiddleware } from 'redux';
// dispatch一个action之后，到达reducer之前，进行一些额外的操作，就需要用到middleware。换言之，中间件都是对store.dispatch()的增强
// redux-thunk最重要的思想，就是可以接受一个返回函数的action creator
import thunk from 'redux-thunk'; // 
import reducer from './reducer';

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const store = createStore(reducer, composeEnhancers(
	applyMiddleware(thunk)
));

export default store;