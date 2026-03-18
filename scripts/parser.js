import { parse } from 'url';

const parseUrl = (url) => {
  const result = parse(url);
  return {
    protocol: result.protocol && result.protocol.slice(0, -1),
    host: result.host,
    pathname: result.pathname,
    search: result.search,
    query: new URLSearchParams(result.search).toString(),
    hash: result.hash,
  };
};

export default parseUrl;