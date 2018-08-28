import { Component, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { SubjectService } from '../services/subject.service';

@Component({
  selector: 'app-plate',
  templateUrl: './plate.component.html',
  styleUrls: ['./plate.component.css']
})
export class PlateComponent implements OnInit {

  refreshMetricsSubscription: Subscription
  slots: any;
  chrompacks: any;
  selectedId: String;
  title: String;

  constructor(private subjectService: SubjectService) { }

  ngOnInit() {
    if(!this.selectedId){
      this.fillSettingsDefault();
    }
  }

  fillSettingsDefault() {
    this.subjectService.getMatrixDefault().subscribe(result => {
      this.slots = result;
    }, err => {
      console.error(err);
      //TODO exibir modal de erro
    });
  }

  viewSlots(chrompack){

    this.selectedId = chrompack._id;
    this.title = chrompack.title;

    this.subjectService.getMatrixAll(this.selectedId).subscribe(result => {
      this.slots = result;
    }, err => {
      console.error(err);
      //TODO exibir modal de erro
    });
  }

}
