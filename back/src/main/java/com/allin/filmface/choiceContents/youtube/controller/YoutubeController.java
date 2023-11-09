package com.allin.filmface.choiceContents.youtube.controller;


import com.allin.filmface.choiceContents.youtube.entity.Youtube;
import com.allin.filmface.choiceContents.youtube.service.YoutubeService;
import com.allin.filmface.common.ResponseDTO;
import com.allin.filmface.emotion.entity.Emotion;
import com.allin.filmface.emotion.repository.EmotionRepository;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;
@RestController
@RequestMapping("/api/v1")
@AllArgsConstructor
public class YoutubeController {

    @Autowired
    private YoutubeService youtubeService;
    @Autowired
    private EmotionRepository emotionRepository;


    @GetMapping("/youtube/emotion")
    public ResponseEntity<ResponseDTO> getYoutubeVideosBasedOnEmotion(@RequestParam(name = "memberNo") Integer memberNo) {
        // 해당 memberNo의 마지막 emotionResult를 가져옵니다.
        Emotion recentEmotion = emotionRepository.findFirstByMemberNoOrderByEmotionNoDesc(memberNo);
        List<Youtube> youtubeList;
        if (recentEmotion == null) {
            youtubeList = new ArrayList<>();
        } else {
            String emotionResult = recentEmotion.getEmotionResult();
            String query = "";
            switch(emotionResult) {
                case "Sad":
                    query = "슬픔을 극복하기";
                    break;
                case "Angry":
                    query = "화날 때 볼만한 영상";
                    break;
                case "Neutral":
                case "Happy":
                    query = "재밌는 영상";
                    break;
                case "Surprise":
                case "Disgust":
                case "Fear":
                    query = "차분한 영상";
                    break;
                default:
                    youtubeList = new ArrayList<>();
                    return ResponseEntity.ok(new ResponseDTO(HttpStatus.OK, "조회성공", youtubeList));
            }
            youtubeList = youtubeService.getYoutubeContentsByQuery(query, memberNo);
        }

        return ResponseEntity.ok(new ResponseDTO(HttpStatus.OK, "조회성공", youtubeList));
    }
}