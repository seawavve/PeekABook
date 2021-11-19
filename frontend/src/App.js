import * as React from 'react';
import styled from 'styled-components';
import Timeline from '@mui/lab/Timeline';
import TimelineItem from '@mui/lab/TimelineItem';
import TimelineSeparator from '@mui/lab/TimelineSeparator';
import TimelineConnector from '@mui/lab/TimelineConnector';
import TimelineContent from '@mui/lab/TimelineContent';
import TimelineDot from '@mui/lab/TimelineDot';
import Button from '@mui/material/ButtonBase';




const Sidebar = styled.div`
  position: absolute;
  left: 0;
  
`

const Main = styled.div`
  width: 100vw;
  height: 150vh;

  & > iframe {
    width: 100%;
    height: 100%;
  }
`


export default function App() {
  //onClick(v)
  const htmlUrl = [
    './data1.html', './data2.html', './data3.html', './data4.html', './data5.html',
    './data6.html', './data7.html', './data8.html', './data9.html', './data10.html'];
  const [url, setUrl] = React.useState(htmlUrl[0])
  

  // function handleClick(e) {
  //   e.preventDefault();
    
  // }

  const handleClick = (index) => () => {
    setUrl(htmlUrl[index])
  }


  

  return (
    
    <div >
      <Sidebar>
        <Timeline position="right">
          <TimelineItem>
            <TimelineSeparator> 
              <Button onClick={handleClick(0)}>
                <TimelineDot variant="outlined"  />
              </Button>
            <TimelineConnector />
            </TimelineSeparator>
            <TimelineContent>Chapter1</TimelineContent>
          </TimelineItem>
        
          <TimelineItem>
            <TimelineSeparator>
                <Button onClick={handleClick(1)} >
                  <TimelineDot variant="outlined"  />
                </Button>
              <TimelineConnector />
            </TimelineSeparator>
            <TimelineContent>Chapter2</TimelineContent>
          </TimelineItem>
          
          <TimelineItem>
            <TimelineSeparator>
              <Button onClick={handleClick(2)} >
                <TimelineDot variant="outlined"  />
              </Button>
              <TimelineConnector />
            </TimelineSeparator>
            <TimelineContent>Chapter3</TimelineContent>
          </TimelineItem>
          
          <TimelineItem>
            <TimelineSeparator>
              <Button onClick={handleClick(3)} >
                <TimelineDot variant="outlined"  />
              </Button>
              <TimelineConnector />
            </TimelineSeparator>
            <TimelineContent>Chapter4</TimelineContent>
          </TimelineItem>
          
          <TimelineItem>
            <TimelineSeparator>
              <Button onClick={handleClick(4)} >
                <TimelineDot variant="outlined"  />
              </Button>
              <TimelineConnector />
            </TimelineSeparator>
            <TimelineContent>Chapter5</TimelineContent>
          </TimelineItem>

          <TimelineItem>
            <TimelineSeparator>
              <Button onClick={handleClick(5)} >
                <TimelineDot variant="outlined"  />
              </Button>
              <TimelineConnector />
            </TimelineSeparator>
            <TimelineContent>Chapter6</TimelineContent>
          </TimelineItem>

          <TimelineItem>
            <TimelineSeparator>
              <Button onClick={handleClick(6)} >
                <TimelineDot variant="outlined"  />
              </Button>
              <TimelineConnector />
            </TimelineSeparator>
            <TimelineContent>Chapter7</TimelineContent>
          </TimelineItem>

          <TimelineItem>
            <TimelineSeparator>
              <Button onClick={handleClick(7)} >
                <TimelineDot variant="outlined"  />
              </Button>
              <TimelineConnector />
            </TimelineSeparator>
            <TimelineContent>Chapter8</TimelineContent>
          </TimelineItem>

          <TimelineItem>
            <TimelineSeparator>
              <Button onClick={handleClick(8)} >
                <TimelineDot variant="outlined"  />
              </Button>
              <TimelineConnector />
            </TimelineSeparator>
            <TimelineContent>Chapter9</TimelineContent>
          </TimelineItem>

          <TimelineItem>
            <TimelineSeparator>
              <Button onClick={handleClick(9)} >
                <TimelineDot variant="outlined"  />
              </Button>
            </TimelineSeparator>
            <TimelineContent>Chapter10</TimelineContent>
          </TimelineItem>
          

        </Timeline>
      </Sidebar>
      <Main>
        <iframe title="main" src={url} />
      </Main>
    </div>
  );
}
