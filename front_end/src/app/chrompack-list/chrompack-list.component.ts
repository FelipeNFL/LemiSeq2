import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { UploadComponent } from '../upload/upload.component';
import { ChromPackService } from '../services/chrompack.service';
import { ChrompackServiceObservable } from '../services/chrompack-observable.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'chrompack-list',
  templateUrl: './chrompack-list.component.html',
  styleUrls: ['./chrompack-list.component.css']
})
export class ChrompackListComponent implements OnInit {

  @Output() viewSlots = new EventEmitter();
  chrompacks: Array<any>;
  selectedId: string;
  refreshMetricsSubscription: Subscription;

  constructor(private modalService: NgbModal,
              private chrompackService: ChromPackService,
              private chrompackServiceObservable: ChrompackServiceObservable) { }

  ngOnInit() {
    this.refreshMetricsSubscription = this.chrompackServiceObservable.getRefreshResult().subscribe(() => {
      this.getList();
    });

    this.getList();
  }

  refreshSelection(id) {
    this.chrompacks.forEach(chrompack => {

      if (chrompack._id === this.selectedId) {
        chrompack.selected = false;
      }

      if (chrompack._id === id) {
        chrompack.selected = true;
      }
    });
  } 

  select(chrompack) {

    const id = chrompack._id;

    this.refreshSelection(id);
    this.selectedId = id;
    this.viewSlots.emit(chrompack);
  }

  add() {
    this.modalService.open(UploadComponent);
  }

  getList() {
    this.chrompackService.getList().subscribe(result => {
      this.chrompacks = result;
    }, err => {
      console.error(err);
      //TODO exibir modal de erro
    });
  }

  delete() {
    this.chrompackService.delete(this.selectedId).subscribe(() => {
      this.getList();
      this.chrompackServiceObservable.sendRefreshResult();
    }, err => {
      console.error(err);
      //TODO exibir modal de erro
    });
  }
}
